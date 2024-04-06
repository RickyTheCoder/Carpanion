from django.db import models
import uuid
from secrets import token_urlsafe

from django.conf import settings

from core.user.models import User

def generate_client_id():
    return token_urlsafe(settings.COREAPP_CLIENTID_N_BYTES)

def generate_client_secret():
    return token_urlsafe(settings.COREAPP_SECRET_N_BYTES)

# Represents applications that can create OAuth clients
class ApplicationClient(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField(blank=True)

    client_id = models.CharField(max_length=100, unique=True, primary_key=True, default=generate_client_id)
    client_secret = models.CharField(max_length=100, default=generate_client_secret)

    def __str__(self):
        return self.name

class UserApplicationAuthorization(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(ApplicationClient, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    scope = models.CharField(max_length=100)
        
    def __str__(self):
        return f'{self.user} - {self.application}'