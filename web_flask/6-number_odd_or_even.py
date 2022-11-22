#!/usr/bin/python3
"""A module to start a simple flask server"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """A controller to handle route '/python/<text>'"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    """A controller to handle '/number/<n> route'"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """A controller to handle '/numbe_template/<n> route'"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """A controller to handle '/number_odd_even/<n> route'"""
    odd_or_even = 'even'
    if n % 2:
        odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
