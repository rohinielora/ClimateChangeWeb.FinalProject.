from flask import Flask, render_template
from climate_manager.controllers.overview import overview_view
from climate_manager.controllers.impact import impact_view
import sqlite3

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('data.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/overview')
def overview():
    return overview_view(get_db())

@app.route('/impact')
def impact():
    return impact_view(get_db())

if __name__ == '__main__':
    app.run(debug=True)
