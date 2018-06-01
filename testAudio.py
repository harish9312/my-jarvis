import speech_recognition as sr
from gtts import gTTS
from time import ctime
import time 
import os
import sys

f = open('/dev/null', 'w')
os.stdout = f

name = "Guest"
n = 1
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You Said: " + data)
    except sr.UnknownValueError :
        print("Cannot Understand")
        # speak("Sorry I don't have an answer yet. But I will surely ask my Harish to make me able to answer you..!!!")
    except sr.RequestError:
        print("Cannot understand")
        # speak("Sorry I don't have an answer yet. But I will surely ask my Harish to make me able to answer you..!!!")


    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine, Thank you..!!!")
    if "what is the time now" in data:
        speak("Current time is: "+ctime().split(" ")[3])
    if "can I give you a name" in data:
        speak("Yeah sure, let me know please..!! ")
        # time.sleep(2)
        name = recordAudio()
        if(len(name) <= 0):
            speak("You did not gave me the name..!!!, Please say something...!!")
            assistantName =  recordAudio()
        speak("Hurrayyy...!!! My name is "+ assistantName)
    if "ok bye" in data:
        speak("Nice taking with you")
        n = 0

speak("Can I know your name please?")
name = recordAudio()
time.sleep(2)
speak("Hello "+name+", what can I do for you?")

while n:
    data = recordAudio()
    print(data)
    jarvis(data)
