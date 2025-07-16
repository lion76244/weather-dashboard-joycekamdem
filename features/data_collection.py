import json
import os
from datetime import datetime

HISTORY_FILE = "search_history.json"
MAX_HISTORY = 5  # number of recent cities to track

def save_search(city, temp):
    """Save a search record with city and timestamp to a local file."""
    entry = {
        "city": city,
        "temp": temp,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    # Remove duplicates, keep newest first
    history = [h for h in history if h["city"].lower() != city.lower()]
    history.insert(0, entry)
    history = history[:MAX_HISTORY]

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_history():
    """Return the list of recent city searches."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


