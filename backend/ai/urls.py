from django.urls import path
from .views import speech_request  # Import the view

urlpatterns = [
    path('speech_request/', speech_request, name='speech_request'),
]

