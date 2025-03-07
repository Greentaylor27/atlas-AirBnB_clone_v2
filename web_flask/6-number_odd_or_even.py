#!/usr/bin/python3
"""Module that should display two inputs"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n: int):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n: int):
    value = n % 2
    even = render_template('6-number_odd_or_even.html', n=n, message='even')
    odd = render_template('6-number_odd_or_even.html', n=n, message='odd')
    if value == 0:
        return even
    else:
        return odd


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
