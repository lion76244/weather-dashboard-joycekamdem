import json
import os
from datetime import datetime

HISTORY_FILE = "search_history.json"

def save_search(city, temp):
    """Append a new search entry to the JSON file without overwriting previous entries."""
    entry = {
        "city": city,
        "temp": temp,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # Load existing history if file exists
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    else:
        history = []

    # Append the new entry (no deduping, no max cap)
    history.append(entry)

    # Save the updated history
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_history(limit=5):
    """Load the full history but return only the most recent `limit` entries."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
                return history[-limit:][::-1]  # get most recent `limit` entries
            except json.JSONDecodeError:
                return []
    return []
