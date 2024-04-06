from secrets import token_urlsafe

from django.conf import settings
from core.application.models import Application, UserApplicationAuthorization

CLIENTID_N_BYTES = settings.COREAPP_CLIENTID_N_BYTES
SECRET_N_BYTES = settings.COREAPP_SECRET_N_BYTES
