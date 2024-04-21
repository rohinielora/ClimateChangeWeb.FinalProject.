# overview.py
from flask import render_template
from ..models.data import fetch_data

def overview_view(conn):
    data = fetch_data(conn, "temperature")
    return render_template("overview.html", data=data)

# impact.py
from flask import render_template
from ..models.data import fetch_data

def impact_view(conn):
    data = fetch_data(conn, "co2_levels")
    return render_template("impact.html", data=data)
