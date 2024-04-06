from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as DRFSJ_TokenObtainPairSerializer

from core.user.models import User

class TokenObtainPairSerializer(DRFSJ_TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['user_implicit_id'] = str(user.implicit_id)
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token