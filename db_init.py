import sqlite3
import csv

def create_tables(cursor):
    cursor.execute('''CREATE TABLE locations (name TEXT, longitude REAL, latitude REAL, region TEXT, country TEXT)''')
    cursor.execute('''CREATE TABLE history (location_name TEXT, date TEXT, weather_description TEXT, temperature INTEGER)''')

def insert_location_data(cursor, locations):
    for location in locations:
        cursor.execute("INSERT INTO locations VALUES (?, ?, ?, ?, ?)", 
                       (location.name, location.longitude, location.latitude, location.region, location.country))

def load_locations_from_csv(filename):
    locations = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            locations.append((row['name'], float(row['longitude']), float(row['latitude']), row['region'], row['country']))
    return locations

def main():
    conn = sqlite3.connect('climate.db')
    cursor = conn.cursor()
    create_tables(cursor)
    locations = load_locations_from_csv('locations.csv')
    insert_location_data(cursor, locations)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
