from gtts import gTTS
import os


def speak(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)

    # Save text as mp3
    tts.save("output.mp3")

    # Play the mp3 file
    os.system("start output.mp3")


