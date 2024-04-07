import base64
import io, os
from core.env import env
import asyncio
from openai import OpenAI
import pygame


def data_uri_to_blob(data_uri):
    # Split the data URI into parts
    header, data = data_uri.split(',')

    # Get the MIME type
    mime_type = header.split(';')[0].split(':')[1]

    # Decode the base64 data
    byte_string = base64.b64decode(data)

    # Create a BytesIO object and return it
    return io.BytesIO(byte_string), mime_type

def text2text(text):
    # Create an OpenAI client
    client = OpenAI(
        # read from .env.local file
        api_key=env("OPENAI_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-4",
    )
    response = chat_completion.choices[0].message.content
    return response

def text2speech(text):
    client = OpenAI()

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    speech_file_path = "output.mp3"
    with open(speech_file_path, "wb") as f:
        f.write(response.read())

    # play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file_path)
    pygame.mixer.music.play()


def image2text(image_data):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/hustvl/yolos-tiny"
    headers = {"Authorization": f"Bearer {env('HF_API_TOKEN')}"}
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()


if __name__ == "__main__":
    image2text("cat_dog.jpg")
    text2speech(text2text("Say this is a test"))

    # # Create a chat model
    # chat_model = .create(
    #     model="gpt-4-vision-preview",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are a helpful assistant."
    #         },
    #         {
    #             "role": "user",
    #             "content": "Please list all items bought in the attached image of the receipt. Then, for each item, provide the usual expiration days. Also, try to make a give the full name of the item, like Good&Gather Hummus instead of GG Hummus. Lastly, please give the number of days each item could expire in, prefixed with [Least number of days] a positive number. Here are the examples of the output:\n"
    #                 + "1. Good&Gather Yogurt: Usually Expire in 2-3 weeks; [Least number of days] 14\n"
    #                 + "2. Lettuce: Usually Expire in 7-10 days; [Least number of days] 7\n"
    #                 + "3. Canned beans: This is a type of food that can be stored as long as 1-2 years. However, it is still suggested to have it ASAP. [Least number of days] 365\n"
    #                 + "Ambiguous Items: GOOD&GATHER, Smartly\n"
    #                 + "Not food: Blogilates, Basketball, T-shirt\n"
    #         },
    #         {
    #             "role": "assistant",
    #             "content": {
    #                 "type": "image",
    #                 "data": base64_image
    #             }
    #         }
    #     ]
    # )

    # Parse the response
    # ...

import whisper

def load_whisper_model():
    # Load the Whisper model
    # Choose the model size appropriate for your use case and hardware
    model = whisper.load_model("base")
    return model

def transcribe_audio(model, audio_path):
    # Transcribe the audio file using Whisper
    result = model.transcribe(audio_path)
    return result["text"]
    
 # service function for transcription    
import openai

openai.api_key = 'OPENAI_API_KEY'

def transcribe_audio_with_whisper(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcription["text"]

