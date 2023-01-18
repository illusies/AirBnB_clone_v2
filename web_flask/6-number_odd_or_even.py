#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """A function that defines the site index"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """A function that defines the hbnb route function"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """A fuction that prints the value of the variable text"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """
	A fuction that prints the value of the variable text
	or the default value
	"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """A function that checks if n is a number"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """A function that displays a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """A function that displays a HTML page only if n is odd or even"""
    return render_template("6-number_odd_or_even.html", number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
