# gui.py
import tkinter as tk
from api import fetch_current_weather
from features.Simple_Statistics import plot_temperature, plot_humidity
from features.data_collection import save_search, load_history
from features.Trend_detection import log_weather_trend, plot_city_trend
from features.Trend_detection import (
    log_weather_trend,
    plot_city_trend,
    export_trends_to_csv
)


# --- GUI Callback Functions ---
def show_weather():
    city = city_entry.get()
    result = fetch_current_weather(city)

    if "error" in result:
        result_label.config(text=result["error"])
    else:
        display = f"🌤️ Weather in {result['city']}:\n{result['description']}, {result['temp']}°C"
        result_label.config(text=display)

        save_search(city, result["temp"])
        log_weather_trend(city, result["temp"])  # ✅ Track weather over time
        update_history_buttons()

def show_temp_plot():
    city = city_entry.get()
    plot_temperature(city)

def show_humidity_plot():
    city = city_entry.get()
    plot_humidity(city)

def show_trend_plot():
    city = city_entry.get()
    plot_city_trend(city)

def fetch_from_history(city):
    city_entry.delete(0, tk.END)
    city_entry.insert(0, city)
    show_weather()  # ✅ Let show_weather handle all logic

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
root.geometry("420x450")
root.resizable(False, False)

# City entry
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Weather result display
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380, justify="center")
result_label.pack(pady=10)

# Weather button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=show_weather)
get_button.pack()

# Plot buttons
plot_temp_button = tk.Button(root, text="Show Temperature Plot", font=("Arial", 10), command=show_temp_plot)
plot_temp_button.pack(pady=5)

plot_humidity_button = tk.Button(root, text="Show Humidity Plot", font=("Arial", 10), command=show_humidity_plot)
plot_humidity_button.pack(pady=5)

# Trend plot button ✅
trend_button = tk.Button(root, text="Show Trend", font=("Arial", 10), command=show_trend_plot)
trend_button.pack(pady=5)

# History buttons
history_frame = tk.Frame(root)
history_frame.pack(pady=10)
update_history_buttons()

# Start the GUI
root.mainloop()

# Button: Show 7-day trend
tk.Button(root, text="Trend: 7 Days", font=("Arial", 10),
          command=lambda: plot_city_trend(city_entry.get(), days=7)).pack(pady=2)

# Button: Show 30-day trend
tk.Button(root, text="Trend: 30 Days", font=("Arial", 10),
          command=lambda: plot_city_trend(city_entry.get(), days=30)).pack(pady=2)

# Button: Export all trends to CSV
tk.Button(root, text="Export to CSV", font=("Arial", 10),
          command=export_trends_to_csv).pack(pady=2)
