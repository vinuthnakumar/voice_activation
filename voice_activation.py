import speech_recognition as sr
import pyttsx3
import requests
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results from the service.")
            return ""

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The temperature in {city} is {temperature}°C with {weather_desc}."
    else:
        return "City not found."

def set_reminder(reminder):
    with open("reminders.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {reminder}\n")
    speak("Reminder set.")

def main():
    speak("Hello, I am your personal assistant. How can I help you today?")
    while True:
        command = listen().lower()
        if "weather" in command:
            city = command.split("in")[-1].strip()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "remind me to" in command:
            reminder = command.split("remind me to")[-1].strip()
            set_reminder(reminder)
            speak("I've noted that down.")
        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
