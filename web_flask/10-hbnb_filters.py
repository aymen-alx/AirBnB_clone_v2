#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!,...
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """ """
    amenities = list(storage.all('Amenity').values())
    states = list(storage.all('State').values())
    return render_template('10-hbnb_filters.html', tasks=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """ """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
