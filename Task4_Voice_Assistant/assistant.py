import speech_recognition as sr
import pyttsx3
import requests
import json
import datetime
import os

engine = pyttsx3.init()
engine.setProperty("rate", 170)

WEATHER_API_KEY = "PUT_YOUR_OPENWEATHER_API_KEY_HERE"
NEWS_API_KEY = "PUT_YOUR_NEWSAPI_KEY_HERE"

REMINDER_FILE = "reminders.json"

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I could not understand. Please try again.")
        return ""

def save_reminder(reminder_text, reminder_time):
    reminders = []
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            try:
                reminders = json.load(f)
            except:
                reminders = []

    reminders.append({"text": reminder_text, "time": reminder_time})

    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f, indent=4)

def show_reminders():
    if not os.path.exists(REMINDER_FILE):
        speak("You have no reminders.")
        return

    with open(REMINDER_FILE, "r") as f:
        reminders = json.load(f)

    if len(reminders) == 0:
        speak("You have no reminders.")
        return

    speak("Here are your reminders.")
    for r in reminders:
        speak(f"{r['text']} at {r['time']}")

def set_reminder():
    speak("What should I remind you about?")
    reminder_text = listen()

    if reminder_text == "":
        return

    speak("Tell me the reminder time in format HH:MM, for example 18:30")
    reminder_time = listen()

    try:
        datetime.datetime.strptime(reminder_time, "%H:%M")
        save_reminder(reminder_text, reminder_time)
        speak(f"Reminder set for {reminder_time}")
    except:
        speak("Invalid time format. Please try again.")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        speak("Unable to fetch weather details.")
        return

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    speak(f"The weather in {city} is {description} with temperature {temp} degree Celsius.")

def weather_command():
    speak("Which city weather do you want?")
    city = listen()
    if city != "":
        get_weather(city)

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        speak("Unable to fetch news.")
        return

    data = response.json()
    articles = data.get("articles", [])

    if len(articles) == 0:
        speak("No news found.")
        return

    speak("Here are the top 5 news headlines.")
    for i in range(min(5, len(articles))):
        speak(articles[i]["title"])

def check_reminders():
    if not os.path.exists(REMINDER_FILE):
        return

    with open(REMINDER_FILE, "r") as f:
        reminders = json.load(f)

    current_time = datetime.datetime.now().strftime("%H:%M")

    updated_reminders = []
    for r in reminders:
        if r["time"] == current_time:
            speak(f"Reminder: {r['text']}")
        else:
            updated_reminders.append(r)

    with open(REMINDER_FILE, "w") as f:
        json.dump(updated_reminders, f, indent=4)

def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        check_reminders()
        command = listen()

        if "weather" in command:
            weather_command()

        elif "news" in command:
            get_news()

        elif "set reminder" in command or "reminder" in command:
            set_reminder()

        elif "show reminders" in command:
            show_reminders()

        elif "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("Sorry, I can only set reminders, tell weather, or read news.")

if __name__ == "__main__":
    main()
