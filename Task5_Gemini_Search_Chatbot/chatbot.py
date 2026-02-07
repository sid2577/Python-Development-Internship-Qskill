import google.generativeai as genai
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

MEMORY_FILE = "memory.json"

if not GEMINI_API_KEY:
    raise Exception("Missing GEMINI_API_KEY in .env file")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def google_search(query):
    if not GOOGLE_SEARCH_API_KEY or not SEARCH_ENGINE_ID:
        return "Google Search API key or Search Engine ID is missing."

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_SEARCH_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Failed to fetch search results."

    data = response.json()
    items = data.get("items", [])

    if not items:
        return "No search results found."

    results_text = ""
    for i, item in enumerate(items[:5]):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        results_text += f"{i+1}. {title}\n{snippet}\nSource: {link}\n\n"

    return results_text.strip()

def needs_realtime_data(user_input):
    keywords = ["price", "bitcoin", "weather", "news", "today", "current", "latest", "rate", "score", "stock"]
    return any(word in user_input.lower() for word in keywords)

def generate_response(user_input, history):
    prompt = ""

    for msg in history[-10:]:
        prompt += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n"

    if needs_realtime_data(user_input):
        search_results = google_search(user_input)
        prompt += f"\nReal-time Search Results:\n{search_results}\n"

    prompt += f"\nUser: {user_input}\nAssistant:"

    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    history = load_memory()
    print("Gemini Chatbot with Memory + Google Search (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Goodbye!")
            break

        assistant_reply = generate_response(user_input, history)
        print("\nAssistant:", assistant_reply, "\n")

        history.append({"user": user_input, "assistant": assistant_reply})
        save_memory(history)

if __name__ == "__main__":
    main()
