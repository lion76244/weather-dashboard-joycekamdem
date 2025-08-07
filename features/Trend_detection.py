import os
import json
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Set up correct paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "../data")
os.makedirs(DATA_FOLDER, exist_ok=True)

TREND_FILE = os.path.join(DATA_FOLDER, "trend_log.json")
CSV_EXPORT_FILE = os.path.join(DATA_FOLDER, "trend_log_export.csv")

def log_weather_trend(city, temp):
    """Log city, date, and temp to a JSON file for long-term tracking."""
    entry = {
        "city": city,
        "temp": temp,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")  # Now includes time
    }

    if os.path.exists(TREND_FILE):
        with open(TREND_FILE, "r") as f:
            try:
                trends = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Trend log is corrupted. Starting fresh.")
                trends = []
    else:
        trends = []

    trends.append(entry)

    with open(TREND_FILE, "w") as f:
        json.dump(trends, f, indent=2)

def load_city_trends(city):
    """Load all trend entries for a given city."""
    if not os.path.exists(TREND_FILE):
        return []

    with open(TREND_FILE, "r") as f:
        try:
            trends = json.load(f)
            return [t for t in trends if t["city"].lower() == city.lower()]
        except json.JSONDecodeError:
            print("⚠️ Could not load trend log.")
            return []

def filter_trends(trends, days=None):
    """Filter trend data by recent number of days (e.g., 7 for weekly, 30 for monthly)."""
    if days is None:
        return trends

    cutoff = datetime.now() - timedelta(days=days)
    filtered = []
    for entry in trends:
        try:
            entry_date = datetime.strptime(entry["date"], "%Y-%m-%d %H:%M")  # Updated to match new format
            if entry_date >= cutoff:
                filtered.append(entry)
        except Exception:
            continue
    return filtered

def apply_plot_styling(ax, title, ylabel):
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Date & Time", fontsize=11)  # Updated label
    ax.set_ylabel(ylabel, fontsize=11)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_facecolor("#f9f9f9")
    plt.tight_layout()

def plot_city_trend(city, days=None):
    """Plot temperature trend for a city. Optional filter by recent days."""
    trends = load_city_trends(city)
    if not trends:
        print(f"⚠️ No trend data for {city}")
        return

    trends = filter_trends(trends, days)
    if not trends:
        print(f"⚠️ No data for {city} in the last {days} days")
        return

    trends.sort(key=lambda x: x["date"])
    dates = [t["date"] for t in trends]
    temps = [t["temp"] for t in trends]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, temps, marker='o', linestyle='-', color='#2ca02c', linewidth=2, markersize=5)
    title = f"📈 Temperature Trend in {city}"
    if days:
        title += f" (Last {days} Days)"
    apply_plot_styling(ax, title, "Temperature (°C)")
    plt.xticks(rotation=45)
    plt.show()

def export_trends_to_csv():
    """Export all trend log data to CSV."""
    if not os.path.exists(TREND_FILE):
        print("❌ No trend log found.")
        return

    with open(TREND_FILE, "r") as f:
        try:
            trends = json.load(f)
        except json.JSONDecodeError:
            print("❌ Invalid trend log.")
            return

    with open(CSV_EXPORT_FILE, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["city", "temp", "date"])
        writer.writeheader()
        for row in trends:
            writer.writerow(row)

    print(f"✅ Trends exported to {CSV_EXPORT_FILE}")
