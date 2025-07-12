import requests
import os

# Read the API key from the environment variable
api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    raise ValueError("API key not found. Make sure OPENWEATHER_API_KEY is set.")

# Define the city and request URL
city = "New York"
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Set query parameters
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"  # Change to 'imperial' for Fahrenheit
}

# Make the API call
response = requests.get(base_url, params=params)

# Handle response
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}: {data['weather'][0]['description'].capitalize()}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print(f"Error {response.status_code}: {response.text}")

