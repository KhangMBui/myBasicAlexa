import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[random.randint(0, 1)].id)

listener.energy_threshold = 500

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't quite catch that. Please repeat")
        command =""
    except sr.RequestError:
        print("Sorry, but I couldn't quite request a result. Please check your internet connection.")
        command =""
    return command
def run_alexa():
    command = takeCommand()
    print(command)
    #Play music
    if 'play' in command:
        song = command.replace('play ', '')
        talk('Certainly. Playing' + song)
        pywhatkit.playonyt(song)
    #Time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is" + time)
        print("The current time is " + time)
    #date
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today is " + date)
        print("The current time is " + date)
    elif 'how are you' in command:
        talk("I'm good. How about you?")
    elif 'What is your name' in command:
        talk("Just call me Alexa")
    #Wikipedia search
    elif 'wikipedia' in command:
        object = command.replace('wikipedia', '')
        info = wikipedia.summary(object, 4)
        print(info)
        talk(info)
    #Tell a joke
    elif 'joke' in command:
        newJoke = pyjokes.get_joke()
        talk(newJoke)
        print(newJoke)
    #Couldn't comprehend
    elif 'stop' in command:
        quit()
    else:
        talk("I didn't quite get you. Please repeat.")

while True:
    run_alexa()