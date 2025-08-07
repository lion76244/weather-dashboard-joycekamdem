import requests
import os
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def fetch_current_weather(city):
    """Fetch current weather conditions for a city."""
    if not API_KEY:
        return {"error": "❌ API key not found. Make sure OPENWEATHER_API_KEY is set."}

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": city,
                "description": data['weather'][0]['description'].capitalize(),
                "temp": data['main']['temp']
            }
        else:
            return {"error": f"❌ Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"❌ Request failed: {str(e)}"}


def get_forecast_data(city):
    """Fetch 5-day forecast data for a city (used in charting)."""
    if not API_KEY:
        raise ValueError("❌ API key not found. Make sure OPENWEATHER_API_KEY is set.")

    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"❌ Error {response.status_code}: {response.text}")

    return response.json()
