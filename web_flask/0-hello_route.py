#!/usr/bin/python3
"""A module to start a simple flask server"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A controller to handle '/' route """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
