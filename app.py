import sqlite3
from flask import Flask, render_template, g
from climate_manager.weather.controller import location_view, history_view

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('climate.db')
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/location')
def location():
    return location_view()

@app.route('/history')
def history():
    return history_view()

if __name__ == '__main__':
    app.run(debug=True)
