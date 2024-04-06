from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from django.utils import timezone

from .models import (
    ApplicationClient,
    UserApplicationAuthorization
)

from .serializers import (
    ApplicationClientSerializer,
    UserApplicationAuthorizationSerializer
)

from django.contrib.auth.signals import user_logged_in

class ApplicationView(APIView):
    serializer_class = ApplicationClientSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, id=None):
        if not id:
            raise APIException('Client ID is required.', code=400)
        
        try:
            application = ApplicationClient.objects.get(client_id=id)

            serialized = ApplicationClientSerializer(application)
            return Response(serialized.data)
        except ApplicationClient.DoesNotExist:
            raise APIException('Application not found.', code=404)
        

class AuthorizeUserWithApplication(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        client_id = request.data.get('client_id')
        scope = request.data.get('scope')

        try:
            application_client = ApplicationClient.objects.get(client_id=client_id)

            application = UserApplicationAuthorization.objects.get_or_create(
                user=user,
                application=application_client,
            )[0]

            application.scope = scope

            application.save()

            token = AuthToken.objects.create(user)[1]

            print(token)

            return Response({
                'token': token,
            })
        except :
            raise APIException('Application not found.', code=404)

class LoginView(KnoxLoginView):
    def post(self, request, format=None):
        
        client_id = request.data.get('client_id')
        scope = request.data.get('scope')

        if client_id is None:
            raise ValueError("client_id is required", code=400)
        
        application = ApplicationClient.objects.get(client_id=client_id)

        if application is None:
            raise ValueError("Application not found", code=404)

        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = request.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                raise APIException(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=403
                )
        token_ttl = self.get_token_ttl()
        instance, token = AuthToken.objects.create(request.user, token_ttl)
        
        authorization = UserApplicationAuthorization.objects.get_or_create(
            user=request.user,
            application=application
        )[0]

        authorization.scope = scope

        authorization.save()

        user_logged_in.send(sender=request.user.__class__,
                            request=request, user=request.user)
        data = self.get_post_response_data(request, token, instance)
        return Response(data)
