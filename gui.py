import tkinter as tk
from tkinter import ttk

from api import fetch_current_weather
from features.Simple_Statistics import plot_temperature, plot_humidity
from features.data_collection import save_search, load_history
from features.Trend_detection import log_weather_trend, plot_city_trend, export_trends_to_csv


# --- Callback Functions ---
def show_weather():
    city = city_entry.get()
    result = fetch_current_weather(city)

    if "error" in result:
        weather_display.config(text=result["error"])
    else:
        display = f"🌤️ {result['city']}\n{result['description']}, {result['temp']}°C"
        weather_display.config(text=display)

        save_search(city, result["temp"])
        log_weather_trend(city, result["temp"])
        update_history_buttons()

def show_temp_plot():
    city = city_entry.get()
    plot_temperature(city)

def show_humidity_plot():
    city = city_entry.get()
    plot_humidity(city)

def show_trend_plot(days=None):
    city = city_entry.get()
    plot_city_trend(city, days=days)

def fetch_from_history(city):
    city_entry.delete(0, tk.END)
    city_entry.insert(0, city)
    show_weather()

def toggle_history():
    if history_frame.winfo_viewable():
        history_frame.grid_remove()
        history_btn.config(text="📂 Show Recent Cities")
    else:
        history_frame.grid()
        history_btn.config(text="📂 Hide Recent Cities")

def update_history_buttons():
    for widget in history_frame.winfo_children():
        widget.destroy()

    history = load_history()
    if history:
        ttk.Label(history_frame, text="Recent Cities:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")

    for idx, entry in enumerate(history, start=1):
        city_name = entry["city"]
        display = f"{city_name} ({entry['temp']}°C)"
        btn = ttk.Button(history_frame, text=display, command=lambda c=city_name: fetch_from_history(c), style="History.TButton")
        btn.grid(row=idx, column=0, pady=2, sticky="ew")


# --- GUI Setup ---
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("700x700")
root.configure(bg="#dbeeff")  # Weather-like light sky blue

# Styles
style = ttk.Style()
style.theme_use("clam")

# General button style
style.configure("TButton",
                font=("Arial", 10),
                padding=6,
                background="#ffffff",
                foreground="#333",
                borderwidth=1)
style.map("TButton",
          background=[("active", "#add8e6")])

# Primary action button (Get Weather)
style.configure("Accent.TButton",
                font=("Arial", 14, "bold"),
                foreground="white",
                background="#4098ff",
                padding=10)
style.map("Accent.TButton",
          background=[("active", "#2f7de6")])

# History button style
style.configure("History.TButton",
                background="#f0f8ff",
                foreground="#333")

style.configure("TLabel", background="#dbeeff", foreground="#000000")
style.configure("TFrame", background="#dbeeff")

# --- Layout ---
city_entry = ttk.Entry(root, width=35, font=("Arial", 12))
city_entry.grid(row=0, column=0, columnspan=3, padx=20, pady=15)

get_weather_btn = ttk.Button(root, text="🌤️  Get Weather", style="Accent.TButton", command=show_weather)
get_weather_btn.grid(row=1, column=0, columnspan=3, pady=10)

weather_display = ttk.Label(root, text="", font=("Arial", 14, "bold"), anchor="center", justify="center", wraplength=600)
weather_display.grid(row=2, column=0, columnspan=3, pady=20)

# --- Forecast Buttons ---
forecast_frame = ttk.Frame(root)
forecast_frame.grid(row=3, column=0, columnspan=3, pady=10)

ttk.Label(forecast_frame, text="Forecast Tools:", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
ttk.Button(forecast_frame, text="📈 Temperature", command=show_temp_plot).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(forecast_frame, text="💧 Humidity", command=show_humidity_plot).grid(row=1, column=1, padx=10, pady=5)

# --- Trend Buttons ---
trend_frame = ttk.Frame(root)
trend_frame.grid(row=4, column=0, columnspan=3, pady=10)

ttk.Label(trend_frame, text="Trends:", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
ttk.Button(trend_frame, text="📊 Show Trend", command=lambda: show_trend_plot()).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(trend_frame, text="🗓️  7 Days", command=lambda: show_trend_plot(days=7)).grid(row=1, column=1, padx=10, pady=5)
ttk.Button(trend_frame, text="📅 30 Days", command=lambda: show_trend_plot(days=30)).grid(row=1, column=2, padx=10, pady=5)

# --- Export ---
export_frame = ttk.Frame(root)
export_frame.grid(row=5, column=0, columnspan=3, pady=10)
ttk.Button(export_frame, text="💾 Export to CSV", command=export_trends_to_csv).pack()

# --- History Toggle Button ---
history_btn = ttk.Button(root, text="📂 Show Recent Cities", command=toggle_history)
history_btn.grid(row=6, column=0, columnspan=3, pady=10)

# --- History Frame (hidden initially) ---
history_frame = ttk.Frame(root)
history_frame.grid(row=7, column=0, columnspan=3, pady=10, sticky="ew")
update_history_buttons()
history_frame.grid_remove()  # Start hidden

# Center columns
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
