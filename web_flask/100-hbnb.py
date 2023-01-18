#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A function that filters the HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states,
						   amenities=amenities,
						   places=places)

@app.teardown_appcontext
def close_storage(exc):
    """A function that removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
