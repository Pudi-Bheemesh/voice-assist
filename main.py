import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 150)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()

speak("Hello there. My name is Sandy, How can I help you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you":
    speak("I am having a good day")
speak("how can i help you??")


