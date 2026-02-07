# Task 4 - Voice Activated Personal Assistant

## Project Description
This is a Python-based Voice Activated Personal Assistant that can:
- Set reminders
- Show reminders
- Check weather
- Read top news headlines

It uses Speech Recognition and Text-to-Speech libraries for interaction.

## Requirements
Install dependencies:

```bash
pip install -r requirements.txt
```

## Run
```bash
python assistant.py
```

## Features
### Weather
Uses OpenWeather API to fetch live weather.

### News
Uses NewsAPI to fetch top headlines.

### Reminders
Stores reminders in a JSON file and alerts when time matches system time.

## Setup API Keys
Replace these in `assistant.py`:

```python
WEATHER_API_KEY = "PUT_YOUR_OPENWEATHER_API_KEY_HERE"
NEWS_API_KEY = "PUT_YOUR_NEWSAPI_KEY_HERE"
```

Get keys from:
- https://openweathermap.org/api
- https://newsapi.org/

## Example Commands
- "weather"
- "news"
- "set reminder"
- "show reminders"
- "exit"

## Note
If PyAudio installation fails on Windows, try:

```bash
pip install pipwin
pipwin install pyaudio
```
