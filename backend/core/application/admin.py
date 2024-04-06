from django.contrib import admin

from core.application.models import (
    ApplicationClient, 
    UserApplicationAuthorization
)

admin.site.register(ApplicationClient)
admin.site.register(UserApplicationAuthorization)