
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='en')
    name = "ahmed.mp3"
    tts.save(name)
    playsound.playsound(name)


def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        tell = ""
        try:
            tell = r.recognize_google(audio)
            print(tell)
        except Exception as e:
            print("oh! sorry, I didn't get that read : " + str(e))
    return tell


print('start')


text = getAudio()
if "hello" in text:
    speak("hello, how are you")
