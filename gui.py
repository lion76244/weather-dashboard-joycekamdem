import tkinter as tk
import requests
import os
from dotenv import load_dotenv
from features.Simple_Statistics import plot_temperature, plot_humidity

# Load environment variables
load_dotenv()

# --- Functions ---
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "❌ API key not found. Make sure OPENWEATHER_API_KEY is set."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
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

def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

def show_temp_plot():
    city = city_entry.get()
    plot_temperature(city)

def show_humidity_plot():
    city = city_entry.get()
    plot_humidity(city)

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x300")
root.resizable(False, False)

# City entry
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Weather result label
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=10)

# Weather fetch button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
get_button.pack()

# Plot buttons (✅ defined BEFORE mainloop)
plot_temp_button = tk.Button(root, text="Show Temperature Plot", command=show_temp_plot)
plot_temp_button.pack(pady=5)

plot_humidity_button = tk.Button(root, text="Show Humidity Plot", command=show_humidity_plot)
plot_humidity_button.pack(pady=5)

# ✅ Start GUI loop
root.mainloop()
