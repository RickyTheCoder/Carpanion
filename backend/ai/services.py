import base64
import io, os
from core.env import env
import asyncio
from openai import OpenAI
import pygame


# Create an OpenAI client
client = OpenAI(
    # read from .env.local file
    api_key=env("OPENAI_API_KEY"),
)


def data_uri_to_blob(data_uri):
    # Split the data URI into parts
    header, data = data_uri.split(',')

    # Get the MIME type
    mime_type = header.split(';')[0].split(':')[1]

    # Decode the base64 data
    byte_string = base64.b64decode(data)

    # Create a BytesIO object and return it
    return io.BytesIO(byte_string), mime_type

messages = []
ai_settings = {}
def set_assistant(setting_pair: str):
    setting = {setting_pair.split("=")[0]: setting_pair.split("=")[1]}
    ai_settings.update(setting)
    setting_string = "From now on, you will be a buddy that sits at the shotgun in my car, talking to me like a best friend! You will evolve into an advanced digital road companion, personalizing the interaction with a specific voice and personality in a voice reflecting your personality too. Your personaly is\n"
    for key, value in ai_settings.items():
        setting_string += f"{key}: {value}\n"
    setting_string += "\n"
    print("setting_string:", setting_string)
    if len(messages) > 0:
        # assert messages[0]["role"] == "system"
        if messages[0]["role"] != "system":
            messages.append({"role": "system", "content": setting_string})
        else:
            messages[0] = {"role": "system", "content": setting_string}
    else:
        messages.append({"role": "system", "content": setting_string})

def text2text(text):
    messages.append({"role": "user", "content": text})
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4",
    )
    response = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})
    if len(messages) > 30:
        messages.pop(1)
        messages.pop(2)
    return response

def text2speech(text):

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file("output.mp3")

    #speech_file = io.BytesIO(response.)
    speech_file_path = "output.mp3"
    
    # get the file of output.mp3 as a response to the client
    with open(speech_file_path, "rb") as f:
        response = f.read()

    os.remove(speech_file_path)

    return response


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

def transcribe_audio_v2(audio_path):
    # Transcribe the audio file using Whisper

    audio_file= open(audio_path, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )


    return transcription.text
