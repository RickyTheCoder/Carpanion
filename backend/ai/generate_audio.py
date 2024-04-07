from gtts import gTTS

def create_test_audio(text, lang='en', filename='test_audio.mp3'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Saved test audio file as {filename}")
