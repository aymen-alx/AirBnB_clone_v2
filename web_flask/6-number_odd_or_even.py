#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!
"""

from flask import Flask, escape, render_template
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


@app.route('/number_template/<int:n>')
def numberr(n):
    """ """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if n % 2 == 0:
        status = 'Number: %d is even' % n
        return render_template('6-number_odd_or_even.html', status=status)
    status = 'Number: %d is odd' % n
    return render_template('6-number_odd_or_even.html', status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
