from django.core.management.base import BaseCommand
from gtts import gTTS

class Command(BaseCommand):
    help = 'Generate an audio file from text for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument('text', type=str, help='Text to convert to speech')

    def handle(self, *args, **options):
        text = options['text']
        tts = gTTS(text=text, lang='en')
        filename = 'test_audio.mp3'
        tts.save(filename)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated audio file {filename}'))
