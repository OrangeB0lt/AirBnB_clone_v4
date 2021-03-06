#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/3-hbnb')
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    amenities = sorted(storage.all('Amenity').values(), key=lambda a: a.name)
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    cities = {
        state.id: sorted(state.cities, key=lambda c: c.name)
        for state in states
    }
    return render_template(
        '3-hbnb.html',
        amenities=amenities,
        cache_id=str(uuid.uuid4()),
        cities=cities,
        states=states
    )

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host='0.0.0.0', port=5000)
