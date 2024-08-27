import pyttsx3 as p
import speech_recognition as sr
from News import *
import randfacts
from jokes import *

engine =p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
def speak (text):
    engine.say(text)
    engine.runAndWait()


r=sr.Recognizer()

speak("hello there I am your voice assisstant . How are you?")

try:
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening..")
        audio=r.listen(source)
        text=r.recognize_google(audio)
        print(text)

except:
    print("Audio not Recognised")


if "what" and "about" and "you" in text:
    speak("I am having a good day sir")
speak("What can i do for you?")

try:
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening....")
        audio=r.listen(source)
        text2=r.recognize_google(audio)
        print(text2)

except:
    print("Audio not recognised")

if "news" in text2:    
    print("Sure sir, Now I will read news for you .")
    speak("Sure sir, Now I will read news for you .")
    arr= news()
    for i in range(len(arr)):
        speak(arr[i])
        print(arr[i])

elif "joke" or "jokes" in text2:
    speak("Sure sir, get ready for some chuckles.")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "fact" or "facts" in text2:
    speak("Sure sir,")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that," +x)
