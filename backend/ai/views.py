from django.shortcuts import render
from core.env import env
import base64

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated


import openai
import speech_recognition as sr
from .services import text2speech, text2text, image2text

# speech_recognition handles the speech-to-text conversion
def speech_to_text(audio_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        # Speech was unintelligible
        return "Could not understand audio"
    except sr.RequestError as e:
        # Could not request results from Google Speech Recognition service
        return f"Could not request results; {e}"
    
    
import openai

# Use Open API key to use library to send converted text to GPT of processing 

openai.api_key = env('OPENAI_API_KEY')

def process_with_gpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another appropriate engine
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

from django.http import JsonResponse
from .services import load_whisper_model, transcribe_audio
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

model = load_whisper_model()

class TranscribeAudioView(APIView):
    def post(self, request):
        if request.FILES.get('audio'):
            audio_file = request.FILES['audio']
            file_name = default_storage.save(audio_file.name, audio_file)
            file_path = default_storage.path(file_name)

            transcription = transcribe_audio(model, file_path)
            response = text2text(transcription)
            text2speech(response)
            # Clean up the audio file if no longer needed
            default_storage.delete(file_name)

            return Response({'transcription': transcription})
        
        raise APIException('Audio file is required.', code=400)
        
#ensure that Django view can parse JSON data correctly

from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

class ImageToTextView(APIView):
    @parser_classes((JSONParser,))
    def post(self, request):
        image_data = request.data.get('image')
        print('image_data obtained from postman')
        import time; time.sleep(5)
        print(type(image_data))
        print(image_data)
        if not image_data:
            raise APIException('Image URL is required.', code=400)
        # base64 encode the image data byte string
        base64_image = base64.b64decode(image_data.read())
        print(base64_image[:100])

        output = image2text(base64_image)
        return Response({'output': output})
