# Task 5 - Gemini Chatbot with Memory + Google Search API

## Project Description
This project integrates Google Gemini using the Google Generative AI API.
It also implements:
- Conversation memory stored in JSON file
- Real-time query answering using Google Search API (Custom Search)

The chatbot can answer queries like:
- Current Bitcoin price
- Weather in Mumbai
- Latest news headlines

## Folder Structure
```
Task5_Gemini_Search_Chatbot/
│── chatbot.py
│── memory.json
│── requirements.txt
│── README.md
```

## Installation
```bash
pip install -r requirements.txt
```

## Setup API Keys
Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_SEARCH_API_KEY=your_google_search_api_key_here
SEARCH_ENGINE_ID=your_custom_search_engine_id_here
```

## How to Run
```bash
python chatbot.py
```

## Features
### Conversation Memory
The bot stores previous messages and responses inside `memory.json`.

### Real-time Search Integration
For real-time queries, the bot fetches latest information using Google Search API.

## Example Questions
- What is the current price of Bitcoin?
- What is the weather in Mumbai today?
- Latest news about AI?

## Notes
You must enable Google Custom Search API and create a Search Engine ID.
