from flask import render_template
from .action import create_location_profile, create_weather_history

def location_view():
    location = create_location_profile("Springfield", -72.589811, 42.101483, "Northeast", "USA")
    return render_template("location.html", location=location)

def history_view():
    location = create_location_profile("Springfield", -72.589811, 42.101483, "Northeast", "USA")
    history = create_weather_history(location, "2024-04-01", "Partly cloudy", 15)
    location.add_history(history)
    return render_template("history.html", location=location)
