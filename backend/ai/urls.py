from django.urls import path
from .views import speech_request  # Import the view
from .views import transcribe_audio_request

urlpatterns = [
    path('speech_request/', speech_request, name='speech_request'),
    path('transcribe_audio/', transcribe_audio_request, name='transcribe_audio'),
    path('your-url/', speech_request, name='speech_request')
]

