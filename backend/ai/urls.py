from django.urls import path
from .views import speech_request  # Import the view
from .views import transcribe_audio

urlpatterns = [
    path('speech_request/', speech_request, name='speech_request'),
    path('transcribe_audio/', transcribe_audio, name='transcribe_audio'),
]

