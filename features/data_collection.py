import json
import os
from datetime import datetime

# Ensure we always use the correct path to the data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "../data")
HISTORY_FILE = os.path.join(DATA_FOLDER, "search_history.json")

# Create the data folder if it doesn't exist
os.makedirs(DATA_FOLDER, exist_ok=True)

def save_search(city, temp):
    """Save a weather search with city name, temperature, and timestamp."""
    if not city or temp is None:
        print("⚠️ Invalid city or temperature. Skipping save.")
        return

    entry = {
        "city": city,
        "temp": temp,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # Load existing history or start a new list
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ History file is corrupted. Starting with an empty list.")
                history = []
    else:
        history = []

    # Append new entry
    history.append(entry)

    # Save updated history back to file
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_history(limit=5):
    """Load the most recent `limit` weather searches."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
                return history[-limit:][::-1]  # most recent first
            except json.JSONDecodeError:
                print("⚠️ Unable to load history. File may be corrupted.")
                return []
    return []
