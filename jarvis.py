import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    print("Starting AI Assistant...")
    speechtx("Hello, I am Jarvis. How can I help you?")
    reminders = []

    while True:
        command = sptext().lower()

        if "your name" in command:
            speechtx("My name is Jarvis.")

        elif "how old are you" in command:
            speechtx("I am two years old.")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(f"The time is {time}.")

        elif "youtube" in command:
            speechtx("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "web" in command:
            speechtx("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif "joke" in command:
            joke = pyjokes.get_joke()
            speechtx(joke)

        elif "open notepad" in command:
            speechtx("Opening Notepad...")
            os.system("notepad")

        elif "shutdown" in command:
            speechtx("Shutting down the system.")
            os.system("shutdown /s /t 1")

        elif "exit" in command or "bye" in command:
            speechtx("Goodbye! Have a nice day.")
            break
