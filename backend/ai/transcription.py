# backend/ai/transcription.py

import whisper

model = whisper.load_model("base")  # Load the Whisper model

def transcribe(audio_file_path):
    # Run the transcription process
    result = model.transcribe(audio_file_path)
    return result["text"]

