import webbrowser
import speech_recognition as sr
import pyttsx3 as p
import time
import webbrowser
from time import ctime
import requests

engine = p.init()
engine.setProperty('rate', 165)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def sandy_speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def joke():
    url = "https://official-joke-api.appspot.com/random_joke" 
    json_data = requests.get(url).json()

    arr=["",""]
    arr[0] = json_data["setup"]
    arr[1] = json_data["punchline"]
    return arr

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio_1 = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio_1)
        except sr.UnknownValueError:
            sandy_speak('Sorry,i did not get that')
        except sr.RequestError:
            sandy_speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
        if 'your name' in voice_data:
                sandy_speak('My name is sandy')
        if 'time' in voice_data:
                sandy_speak(ctime())
        if 'where do you live' in voice_data:
                sandy_speak('i live in your computer and it is getting running out of space')
        if 'search' in voice_data:
                sandy_speak('what do you want to search for?')
                search = record_audio()
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                sandy_speak('here is what I found for ' + search)
        if 'find location' in voice_data:
                sandy_speak('which location are you searching for?')
                location = record_audio()
                url_2 = 'https://google.nl/maps/place/' + location + '/&amp'
                webbrowser.get().open(url_2)
                sandy_speak('here is the location of ' + location)
        if 'youtube' and 'video' in voice_data:
                sandy_speak("which video do you want in youtube?")
                result = record_audio()
                sandy_speak("here is the search of " + result)
                url_3 = 'https://www.youtube.com/results?search_query=' + result
                webbrowser.get().open(url_3)

        if 'joke' in voice_data:
                sandy_speak('Sure, Get ready for some chuckles')
                arr = joke()
                sandy_speak(arr[0])
                sandy_speak(arr[1])
        
        if 'thank you' in voice_data:
                sandy_speak('your welcome. I will take leave.')
                exit()


time.sleep(1)
sandy_speak('Hello there, I am sandy. How can I help you ?')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)