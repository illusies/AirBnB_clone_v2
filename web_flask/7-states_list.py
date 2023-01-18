#!/usr/bin/python3
"""A script that updates parts of our engine"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'

@app.route('/states_list', strict_slashes=False)
def states_list():
    """A function that updates the state list"""
    template = '7-states_list.html'
    states = storage.all(State).values()
    return render_template(template, states=states)

@app.teardown_appcontext
def close_storage(exc):
    """A function that removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
