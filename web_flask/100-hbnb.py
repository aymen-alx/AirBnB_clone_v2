#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!,...
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """ """
    places = list(storage.all('Place').values())
    cities = list(storage.all('City').values())
    users = list(storage.all('User').values())
    states = list(storage.all('State').values())
    amenities = list(storage.all('Amenity').values())
    return render_template('100-hbnb.html', tasks=states, amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def teardown(self):
    """ """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
