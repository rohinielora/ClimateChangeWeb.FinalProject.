from climate_manager.models.location import Location
from climate_manager.models.history import History

def create_location_profile(name, longitude, latitude, region, country):
    return Location(name, longitude, latitude, region, country)

def create_weather_history(location, date, description, temperature):
    return History(location, date, description, temperature)
