#!/usr/bin/python3

from flask import Flask, jsonify
from models.city import City
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/cities')
def cities():
    """ Prints out all cities data """

    # Load some data here for testing purposes
    # Note that we are appending dictionaries instead of City objects
    cities_list = []
    cities_list.append(City(name="Gotham").__dict__)
    cities_list.append(City(name="Metropolis", country_id=1).__dict__)
    cities_list.append(City(country_id=2).__dict__)

    return cities_list

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
