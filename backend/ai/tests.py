import os
from django.test import TestCase
from ai.transcription import transcribe

class TranscriptionTestCase(TestCase):
    def test_transcription(self):
        audio_file_path = r'C:\Users\river\Carpanion\backend\test_audio.mp3'
        print(f"Checking for file at: {audio_file_path}")
        self.assertTrue(os.path.isfile(audio_file_path), "Test audio file does not exist.")

        transcription = transcribe(audio_file_path)
        self.assertIsNotNone(transcription)

