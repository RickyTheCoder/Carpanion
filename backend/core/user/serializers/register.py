from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from dj_rest_auth.registration.serializers import RegisterSerializer

from allauth.account.adapter import get_adapter
from allauth.socialaccount.models import SocialAccount, EmailAddress

class UserRegisterSerializer(RegisterSerializer):
    """
    Serializer for user creation
    """

    username = None

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }
    
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and EmailAddress.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                _('A user is already registered with this e-mail address.'),
            )
        return email
