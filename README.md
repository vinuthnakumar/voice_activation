

Personal Voice Assistant

This repository contains the code for a simple personal voice assistant built using Python. This assistant can perform basic tasks like telling you the weather and setting reminders, all through voice commands.

Features
Voice Recognition: Understands your commands using Google's Speech Recognition API.
Text-to-Speech: Responds to you audibly.
Weather Information: Fetches current weather details for any city (requires an API key).
Reminder Setter: Helps you set and store reminders.
Getting Started
Follow these steps to get your personal voice assistant up and running.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
pip (Python package installer)
Installation
Clone the repository:

Bash

git clone https://github.com/vinuthnakumar/personal-voice-assistant.git
cd personal-voice-assistant
Install the required Python packages:

Bash

pip install SpeechRecognition pyttsx3 requests
Get an OpenWeatherMap API Key:
To use the weather feature, you'll need a free API key from OpenWeatherMap.

Go to https://openweathermap.org/api
Sign up for a free account.
Generate your API key.
Update the API Key in the code:
Open the main.py (or the name of your Python script if different) file and replace "YOUR_API_KEY" with your actual OpenWeatherMap API key in the get_weather function:

Python

def get_weather(city):
    api_key = "YOUR_API_KEY" # <--- Replace this
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # ... rest of the code
Running the Assistant
Execute the Python script from your terminal:

Bash

python main.py
The assistant will greet you and start listening for commands.

How to Use
Once the assistant is running, you can speak the following commands:

"What's the weather in [City Name]?" (e.g., "What's the weather in London?")
"Remind me to [Your Reminder]" (e.g., "Remind me to call John at 3 PM")
"Exit" (to stop the assistant)
Code Structure
main.py: The main script containing the voice assistant's logic.
speak(text): Converts text to speech.
listen(): Captures audio from the microphone and converts it to text.
get_weather(city): Fetches weather information using the OpenWeatherMap API.
set_reminder(reminder): Saves reminders to a reminders.txt file.
main(): The core loop of the assistant, handling commands.
reminders.txt: (Will be created automatically) Stores your set reminders.
