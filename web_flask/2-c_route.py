#!/usr/bin/python3
"""A module to start a simple flask server"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A controller to handle '/' route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A controller to handle '/hbnb' route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """A controller to handle route '/c/<text>'"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
