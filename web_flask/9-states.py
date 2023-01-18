#!/usr/bin/python3
"""A script that starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """A function that filters the cities/state list"""
    template = '9-states.html'
    states = storage.all(State)
    key = None if id is None else 'State.{id}'.format(id=id)
    return render_template(template, states=states, key=key)

@app.teardown_appcontext
def close_storage(exc):
    """A function that removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
