#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """A function that lists the cities by state"""
    template = '8-cities_by_states.html'
    states = storage.all(State).values()
    return render_template(template, states=states)

@app.teardown_appcontext
def close_storage(exc):
    """A function that removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
