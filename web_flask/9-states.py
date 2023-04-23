#!/usr/bin/python3
"""
Hello Flask!, HBNB, C is fun!,...
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """ """
    state = list(storage.all('State').values())
    return render_template('7-states_list.html', states=state)


@app.route('/states/<id>')
def states_by_id(id):
    """ """
    temporary = []
    states = list(storage.all('State').values())
    for state in states:
        if state.id == id:
            temporary.append(state)
            return render_template(
                '9-states.html', statess=temporary, name=state.name)
    return render_template('9-states.html', statess=None)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
