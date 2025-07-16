import requests
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_forecast_data(city):
    if not api_key:
        raise ValueError("❌ API key not found. Make sure OPENWEATHER_API_KEY is set.")

    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"❌ Error {response.status_code}: {response.text}")

    return response.json()

def plot_temperature(city):
    data = get_forecast_data(city)
    times = [entry["dt_txt"] for entry in data["list"]]
    temps = [entry["main"]["temp"] for entry in data["list"]]

    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o', linestyle='-', color='orange')
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Temperature Forecast for {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def plot_humidity(city):
    data = get_forecast_data(city)
    times = [entry["dt_txt"] for entry in data["list"]]
    humidity = [entry["main"]["humidity"] for entry in data["list"]]

    plt.figure(figsize=(10, 5))
    plt.plot(times, humidity, marker='x', linestyle='-', color='blue')
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Humidity Forecast for {city}")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    plot_temperature(city_name)
    plot_humidity(city_name)
