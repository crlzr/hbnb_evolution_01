#!/usr/bin/python3

from flask import Flask, jsonify
from models.city import City
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/cities_example')
def cities_example():
    """ Creates some City data for testing purposes """

    # Note that we are appending dictionaries instead of City objects
    cities_list = []
    cities_list.append(City(name="Gotham").__dict__)
    cities_list.append(City(name="Metropolis", country_id=1).__dict__)

    # The city with the invalid name is not appended to cities_list
    try:
        cities_list.append(City(name="#$%^&**", country_id=2).__dict__)
    except ValueError as exc:
        # This is printed internally in the server output. Not shown on website.
        print("City creation Error - ", exc)

    return cities_list

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
