from rest_framework import serializers

from core.application.models import ApplicationClient, UserApplicationAuthorization

class ApplicationClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationClient
        fields = [
            'name',
            'text',
            'client_id',
            'created_at',
            'updated_at'
        ]

class UserApplicationAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApplicationAuthorization
        fields = [
            'user',
            'application',
            'created_at',
            'updated_at',
            'scope'
        ]