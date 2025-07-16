import tkinter as tk
import requests
import os
from dotenv import load_dotenv
from features.Simple_Statistics import plot_temperature, plot_humidity
from features.data_collection import save_search, load_history

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# --- Weather fetch function ---
def get_weather(city):
    if not API_KEY:
        return "❌ API key not found. Make sure OPENWEATHER_API_KEY is set."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        return f"🌤️ Weather in {city}:\n{weather}, {temp}°C"
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# --- GUI Callback Functions ---
def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

    if "🌤️" in result:
        try:
            temp = result.split(",")[-1].strip("°C")
            save_search(city, temp)
            update_history_buttons()
        except Exception as e:
            print(f"⚠️ Could not save history: {e}")

def show_temp_plot():
    city = city_entry.get()
    plot_temperature(city)

def show_humidity_plot():
    city = city_entry.get()
    plot_humidity(city)

def fetch_from_history(city):
    city_entry.delete(0, tk.END)
    city_entry.insert(0, city)
    show_weather()

def update_history_buttons():
    for widget in history_frame.winfo_children():
        widget.destroy()

    history = load_history()
    if history:
        history_label = tk.Label(history_frame, text="Recent Cities:", font=("Arial", 10, "bold"))
        history_label.pack()

    for entry in history:
        city_name = entry["city"]
        display = f"{city_name} ({entry['temp']}°C)"
        btn = tk.Button(history_frame, text=display, font=("Arial", 10), command=lambda c=city_name: fetch_from_history(c))
        btn.pack(pady=2)

# --- GUI Layout ---
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("420x400")
root.resizable(False, False)

# Entry for city name
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Weather result label
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380, justify="center")
result_label.pack(pady=10)

# Get weather button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
get_button.pack()

# Plot buttons
plot_temp_button = tk.Button(root, text="Show Temperature Plot", font=("Arial", 10), command=show_temp_plot)
plot_temp_button.pack(pady=5)

plot_humidity_button = tk.Button(root, text="Show Humidity Plot", font=("Arial", 10), command=show_humidity_plot)
plot_humidity_button.pack(pady=5)

# Frame for history buttons
history_frame = tk.Frame(root)
history_frame.pack(pady=10)
update_history_buttons()

# Start GUI
root.mainloop()
