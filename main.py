# main.py
"""
Main entry point for the Weather Dashboard application.
This script launches the GUI, which integrates:
- Real-time weather API fetching
- Temperature and humidity forecasting
- Trend detection and logging
- CSV export of trend logs
- Search history and recent city buttons
"""

from gui import root

if __name__ == "__main__":
    root.mainloop()
