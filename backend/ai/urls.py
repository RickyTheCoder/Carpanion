from django.urls import path
from .views import speech_to_text  # Import the view
from .views import transcribe_audio, TranscribeAudioView

urlpatterns = [
    path('speech_request/', speech_to_text, name='speech_request'),
    path('transcribe_audio/', TranscribeAudioView.as_view(), name='transcribe_audio'),
]

