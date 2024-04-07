from django.urls import path
from .views import speech_to_text  # Import the view
from .views import transcribe_audio, TranscribeAudioView, ImageToTextView, ConversationView

urlpatterns = [
    path('speech_request/', speech_to_text, name='speech_request'),
    path('transcribe_audio/', TranscribeAudioView.as_view(), name='transcribe_audio'),
    path('image_to_text/', ImageToTextView.as_view(), name='image_to_text'),
    path('conversation/', ConversationView.as_view(), name='conversation'),
]

