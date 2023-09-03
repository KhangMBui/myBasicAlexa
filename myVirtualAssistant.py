import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import random
import webbrowser
import winshell
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[random.randint(0, 1)].id)
listener.energy_threshold = 500
botName = 'Alexa'

def greetings():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        talk("Good morning.")
    elif time>=12 and time<15:
        talk("Good afternoon.")
    else:
        talk("Good evening.")
    talk("I am your virtual assistant, " + botName + ". How can I assist you today, my master?")


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
            if botName in command:
                command = command.replace(botName, '')
                talk(command)
    except Exception as e:
        print(e)
        print("I didn't quite catch that. Please repeat")
        command = ""
    # except sr.UnknownValueError:
    #     print("Sorry, I didn't quite catch that. Please repeat")
    #     command =""
    # except sr.RequestError:
    #     print("Sorry, but I couldn't quite request a result. Please check your internet connection.")
    #     command =""
    return command
def run_alexa():
    command = takeCommand().lower();
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
        print("The current time is" + date)
    #Daily conversation
    elif 'how are you' in command:
        talk("I'm good. How about you?")
    # elif 'good' or 'fine' in command:
    #     talk("I'm glad to find that you feel well")
    elif 'what is your name' in command:
        talk("Just call me" + botName)
    elif 'what is your purpose' in command:
        talk("I'm here to assist you my master")
    #Wikipedia search
    elif 'wikipedia' in command:
        talk('Searching wikipedia...')
        command = command.replace('wikipedia', '')
        info = wikipedia.summary(object, 3)
        talk('According to wikipedia')
        print(info)
        talk(info)
    #Brower/Application opening:
    elif ('open google chrome') in command:
        try:
            path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        except FileNotFoundError as e:
            talk("Couldn't find the file specified.")
            print("Coudldn't find the file specified.")
        except FileExistsError as e:
            talk("File doesn't exist.")
            print("File doesn't exist.")
    elif ('open excel') in command:
        try:
            path = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(path)
        except FileNotFoundError as e:
            talk("Couldn't find the file specified.")
            print("Coudldn't find the file specified.")
        except FileExistsError as e:
            talk("File doesn't exist.")
            print("File doesn't exist.")
    elif ('open visual studio') in command:
        try:
            path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
            os.startfile(path)
        except FileNotFoundError as e:
            talk("Couldn't find the file specified.")
            print("Coudldn't find the file specified.")
        except FileExistsError as e:
            talk("File doesn't exist.")
            print("File doesn't exist.")
    elif ('open visual studio code') in command:
        try:
            path = r"C:\Users\khang\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)
        except FileNotFoundError as e:
            talk("Couldn't find the file specified.")
            print("Coudldn't find the file specified.")
        except FileExistsError as e:
            talk("File doesn't exist.")
            print("File doesn't exist.")
    elif ('open py charm') in command:
        try:
            path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\bin\pycharm64.exe"
            os.startfile(path)
        except FileNotFoundError as e:
            talk("Couldn't find the file specified.")
            print("Coudldn't find the file specified.")
        except FileExistsError as e:
            talk("File doesn't exist.")
            print("File doesn't exist.")


    #Website opening:
    elif 'open google' in command:
        talk('Opening Google')
        webbrowser.open("https://google.com")
    elif ('open youtube') in command:
        talk('Opening Youtube')
        webbrowser.open("https://youtube.com")
    elif ('open leet code') in command:
        talk('Opening leet code')
        webbrowser.open("https://leetcode.com/")
    elif ('open facebook') in command:
        talk('Opening facebook')
        webbrowser.open("https://facebook.com/")
    elif ('open instagram') in command:
        talk('Opening instagram')
        webbrowser.open("https://instagram.com/")
    #Clear recycle bin
    elif ('empty recycle bin') in command:
        #the parameter in the method: (Confirmation, show progress, sound)
        #The first false so that it wouldn't ask me for confirmation before clearing the bin
        winshell.recycle_bin().empty(False, True, True)
        talk("Recycle bin cleared")
    #Tell a joke
    elif 'joke' in command:
        new_joke = pyjokes.get_joke()
        talk(new_joke)
        print(new_joke)
    #Couldn't comprehend
    elif 'stop' in command:
        quit()
    else:
        talk("I didn't quite get you. Please repeat.")

greetings()
while True:
    run_alexa()