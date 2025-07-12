import tkinter as tk
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to get weather data
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "❌ API key not found. Make sure OPENWEATHER_API_KEY is set."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        return f"🌤️ Weather in {city}:\n{weather}, {temp}°C"
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# Function to update the result label
def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x250")
root.resizable(False, False)

# City input field
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=20)
city_entry.insert(0, "Enter city name")

# Button to get weather
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
get_button.pack()

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=20)

# Run the app
root.mainloop()
