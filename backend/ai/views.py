from django.shortcuts import render
from core.env import env
import base64

import requests

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated


import openai
import speech_recognition as sr
from .services import text2speech, text2text, image2text, transcribe_audio_with_whisper, transcribe_audio, transcribe_audio_v2, set_assistant

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

def get_location(lat, lon):
    api_ninja_key = env('APININJA_API')

    if not lat or not lon:
        return None
    
    response = requests.get(f'https://api.api-ninjas.com/v1/reversegeocoding?lat={lat}&lon={lon}', headers={
        'X-Api-Key': api_ninja_key
    }).json()
    location_data = response[0]    
    return location_data

class ImageToTextView(APIView):
    @parser_classes((JSONParser,))
    def post(self, request):
        
        lat, lon = request.data.get('latitude'), request.data.get('longitude')
        
        location = get_location(lat, lon)

        image_data = request.data.get('image')

        if not image_data:
            raise APIException('Image URL is required.', code=400)
        # base64 encode the image data byte string
        base64_image = base64.b64decode(image_data)

        output = image2text(base64_image)
        
        labels = []

        # for each detection, get the label

        for detection in output:
            labels.append(detection['label'])

        # randomly select a label and generate either a fun fact or a joke

        if labels:
            label = labels[0]
            
            prompt = f"""Tell me a fun fact about {label} or tell me a joke about {label}. Only one of the two will be generated.
            
            """
            
            response = text2text(prompt)

            # get the audio file of the generated text

            audio_file = text2speech(response)

            audio_base64 = base64.b64encode(audio_file).decode('utf-8')
            
            return Response({'output': response, 'audio': audio_base64 })
        
        else:
            if location:
                prompt = f"""
                Generate a fun fact or joke about {location['name']}, {location['country']}, {location.get('state', '')}.
                It should be one of the two, not both.
                """

                response = text2text(prompt)

                audio_file = text2speech(response)

                audio_base64 = base64.b64encode(audio_file).decode('utf-8')

                return Response({'output': response, 'audio': audio_base64 })
            


        raise APIException('No labels detected.', code=400)


class ConversationView(APIView):
    @parser_classes((JSONParser,))
    def post(self, request):
        from pydub import AudioSegment
        
        lat, lon = request.data.get('latitude'), request.data.get('longitude')
        
        location = get_location(lat, lon)

        audio_file = request.data.get('audio')

        if not audio_file:
            raise APIException('Audio is required.', code=400)
        # base64 encode the image data byte string
        base64_audio = base64.b64decode(audio_file)

        # create a audio file from the base64 audio data
        open('audio.m4a', 'wb').write(base64_audio)

        # convert the m4a file to mp3
        audio = AudioSegment.from_file('audio.m4a')
        audio.export('audio.wav', format='wav')

        # use the file path to transcribe the audio

        output = transcribe_audio_v2(audio_path='audio.wav')

        # use the output as a prompt for the GPT model

        try:
            response = text2text(output)

            # get the audio file of the generated text

            audio_file = text2speech(response)

            # write the audio file to a temporary file
            open('output.mp3', 'wb').write(audio_file)

            audio_base64 = base64.b64encode(audio_file).decode('utf-8')

            return Response({'output': response, 'audio': audio_base64 })
        except Exception as e:
            raise APIException(f"Error: {e}", code=400)

    
        # randomly select a label and generate either a fun fact or a joke

        return Response({'output': output})
class SettingsView(APIView):
    def post(self, request):
        setting_string = request.data.get('setting_pair')
        if not setting_string:
            raise APIException('Setting string is required.', code=400)
        set_assistant(setting_string)
