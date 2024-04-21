import sqlite3
import csv
from climate_manager.models.location import Location
from climate_manager.models.history import History

def create_tables(cursor):
    cursor.execute('''CREATE TABLE locations (name TEXT, longitude REAL, latitude REAL, region TEXT, country TEXT)''')
    cursor.execute('''CREATE TABLE history (location_name TEXT, date TEXT, weather_description TEXT
