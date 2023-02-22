#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """removes current sqlachemy"""
    storage.close()


@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """hbnb is alive"""
    states = storage.all(State).value()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(states, key=lambda k: k.name)])

    amenities = storage.all(Amenity).value()
    aminities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).value()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """main function"""
    app.run(host='0.0.0.0', port=5000)
