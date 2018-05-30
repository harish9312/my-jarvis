import speech_recognition as sr
from gtts import gTTS
from time import ctime
import time 
import os

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        print(source)
        audio = r.listen(source)
        print(audio)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You Said: " + data)
    except sr.UnknownValueError :
        print("Cannot Understand")
    except sr.RequestError as e:
        print("Cannot understand")

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
            name =  recordAudio()
        speak("Hurrayyy...!!! My name is "+ name)

print("Please enter your name first...!!!   ")
name = input()
time.sleep(2)
speak("Hello "+name+", what can I do for you?")
while 1:
    data = recordAudio()
    print(data)
    jarvis(data)
