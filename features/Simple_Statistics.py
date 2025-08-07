import plotly.graph_objects as go
from datetime import datetime
from api import get_forecast_data

def plot_temperature(city):
    """Interactive Plotly chart for temperature forecast."""
    data = get_forecast_data(city)
    times = [datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S") for entry in data["list"]]
    temps = [entry["main"]["temp"] for entry in data["list"]]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=times,
        y=temps,
        mode='lines+markers',
        name='Temperature',
        line=dict(color='orange', width=3),
        marker=dict(size=8),
        hovertemplate='Temp: %{y}°C<br>Time: %{x}<extra></extra>'
    ))

    fig.update_layout(
        title=f"🌡️ Temperature Forecast for {city}",
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        plot_bgcolor="#fdfaf6",
        font=dict(family="Arial", size=14),
        hovermode="x unified",
        xaxis=dict(showgrid=True, tickangle=45),
        yaxis=dict(showgrid=True)
    )

    fig.show()

def plot_humidity(city):
    """Interactive Plotly chart for humidity forecast."""
    data = get_forecast_data(city)
    times = [datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S") for entry in data["list"]]
    humidity = [entry["main"]["humidity"] for entry in data["list"]]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=times,
        y=humidity,
        mode='lines+markers',
        name='Humidity',
        line=dict(color='skyblue', width=3),
        marker=dict(size=8),
        hovertemplate='Humidity: %{y}%<br>Time: %{x}<extra></extra>'
    ))

    fig.update_layout(
        title=f"💧 Humidity Forecast for {city}",
        xaxis_title="Time",
        yaxis_title="Humidity (%)",
        plot_bgcolor="#f0fbff",
        font=dict(family="Arial", size=14),
        hovermode="x unified",
        xaxis=dict(showgrid=True, tickangle=45),
        yaxis=dict(showgrid=True)
    )

    fig.show()
