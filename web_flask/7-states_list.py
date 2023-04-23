#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!,...
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ """
    state = list(storage.all('State').values())
    return render_template('7-states_list.html', states=state)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')