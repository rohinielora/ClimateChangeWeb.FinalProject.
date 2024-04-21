import sqlite3
import csv

def create_table(cursor):
    cursor.execute('''CREATE TABLE climate_data (date TEXT, temperature FLOAT, co2_levels FLOAT)''')

def insert_data(cursor, data):
    cursor.executemany("INSERT INTO climate_data VALUES (?, ?, ?)", data)

def load_data_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        return list(reader)

def main():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    create_table(cursor)
    data = load_data_from_csv('data.csv')
    insert_data(cursor, data)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
