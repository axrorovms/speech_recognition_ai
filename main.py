import re

import speech_recognition as sr
import g4f
import concurrent.futures
from gtts import gTTS
import os


def ask_gpt(prompt: str) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )
    return response


def text_to_voice(text, language='ru'):
    tts = gTTS(text=text, lang=language, slow=False)

    # Save text as mp3
    tts.save("output.mp3")

    # Play the mp3 file
    # os.system("start output.mp3")


def process_audio():
    selected_index = 0
    selected_mic = sr.Microphone(device_index=selected_index)
    r = sr.Recognizer()

    with selected_mic as source:
        print("Ask anything from AI")
        audio = r.listen(source)

    try:
        print("Analyzing request")
        a = r.recognize_google(audio, language='ru-RU')
        answer = ask_gpt(a).replace('*', '')
        response = answer.replace(')', '')
        print(response)
        text_to_voice(response)
    except sr.UnknownValueError:
        print('Speech could not be understood..\n Please try again(')

    except sr.RequestError as e:
        print(f'Error occurred: {e}')


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(process_audio)
        future.result()
