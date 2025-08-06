# gui.py
import tkinter as tk
from tkinter import ttk

from api import fetch_current_weather
from features.Simple_Statistics import plot_temperature, plot_humidity
from features.data_collection import save_search, load_history
from features.Trend_detection import log_weather_trend, plot_city_trend, export_trends_to_csv


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
        log_weather_trend(city, result["temp"])
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
    show_weather()

def update_history_buttons():
    for widget in history_frame.winfo_children():
        widget.destroy()

    history = load_history()
    if history:
        history_label = ttk.Label(history_frame, text="Recent Cities:", font=("Arial", 10, "bold"))
        history_label.pack()

    for entry in history:
        city_name = entry["city"]
        display = f"{city_name} ({entry['temp']}°C)"
        btn = ttk.Button(history_frame, text=display, command=lambda c=city_name: fetch_from_history(c))
        btn.pack(pady=2)

# --- GUI Layout ---
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("420x500")
root.resizable(False, False)

# Use modern themed buttons
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Arial", 10), padding=6)
style.configure("Accent.TButton", font=("Arial", 10, "bold"), foreground="white", background="#2b8aed")

# City entry
city_entry = ttk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Weather result display
result_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=380, justify="center")
result_label.pack(pady=10)

# Weather fetch button
ttk.Button(root, text="🌤️ Get Weather", style="Accent.TButton", command=show_weather).pack(pady=5)

# Forecast plots
ttk.Button(root, text="📈 Show Temperature", command=show_temp_plot).pack(pady=2)
ttk.Button(root, text="💧 Show Humidity", command=show_humidity_plot).pack(pady=2)
ttk.Button(root, text="📊 Show Trend", command=show_trend_plot).pack(pady=2)

# Trend time range
ttk.Button(root, text="🗓️ Trend: 7 Days", command=lambda: plot_city_trend(city_entry.get(), days=7)).pack(pady=2)
ttk.Button(root, text="📅 Trend: 30 Days", command=lambda: plot_city_trend(city_entry.get(), days=30)).pack(pady=2)

# Export data
ttk.Button(root, text="💾 Export Trends to CSV", command=export_trends_to_csv).pack(pady=5)

# History section
history_frame = ttk.Frame(root)
history_frame.pack(pady=10)
update_history_buttons()

# Start the GUI
root.mainloop()
