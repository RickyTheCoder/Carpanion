from django.shortcuts import render

# Create your views here.

import openai
import speech_recognition as sr

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

openai.api_key = 'your_openai_api_key'

def process_with_gpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another appropriate engine
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def speech_request(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio']
        file_name = default_storage.save(audio_file.name, audio_file)
        file_path = default_storage.path(file_name)

        text = speech_to_text(file_path)
        response_text = process_with_gpt(text)

        return JsonResponse({'text': text, 'gpt_response': response_text})

    return JsonResponse({'error': 'Request must be POST.'}, status=400)
