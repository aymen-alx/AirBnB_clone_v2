#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!
"""

from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ """
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """ """
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    """ """
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0')
