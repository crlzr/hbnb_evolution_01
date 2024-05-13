#!/usr/bin/python3

from flask import Flask, jsonify
from models.city import City
from data import country_data, place_data, amenity_data, place_to_amenity_data, review_data, user_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/storage_example')
def storage_example():
    """ Example to show that we can view data loaded in the data module's init """
    return jsonify(country_data)

@app.route('/cities_example')
def cities_example():
    """ Example route to showing usage of the City model class """

    # We will be appending dictionaries to the list instead of City objects
    # This is so we can print them out on the webpage
    # If there is no need to display the data, we can consider storing the City objects themselves
    cities_list = []

    # the 'hello' and 'world' params below will be filtered off in City constructor
    cities_list.append(City(name="Gotham", hello="hello").__dict__)
    cities_list.append(City(name="Metropolis", world="world").__dict__)

    # Validation: The city with the invalid name is not appended to the list
    try:
        cities_list.append(City(name="#$%^&**", country_id=2).__dict__)
    except ValueError as exc:
        # This is printed internally in the server output. Not shown on website.
        print("City creation Error - ", exc)

    # Validation: The city with the invalid country_id is not appended to the list
    try:
        cities_list.append(City(name="Duckburg", country_id=1234).__dict__)
    except ValueError as exc:
        print("City creation Error - ", exc)

    # Note that private attributes have a weird key format. e.g. "_City__country_id"
    # This shows that the output of the City object's built-in __dict__ is not usable as-is

    return cities_list

@app.route('/places_amenties_raw_example')
def places_amenities_raw_example():
    """ Prints out the raw data for relationships between places and their amenities """
    return jsonify(place_to_amenity_data)

@app.route('/places_amenties_prettified_example')
def places_amenties_prettified_example():
    """ Prints out the relationships between places and their amenities using names """

    output = {}

    for place_key in place_to_amenity_data:
        place_name = place_data[place_key]['name']
        if place_name not in output:
            output[place_name] = []

        amenities_ids = place_to_amenity_data[place_key]
        for amenity_key in amenities_ids:
            amenity_name = amenity_data[amenity_key]['name']
            output[place_name].append(amenity_name)

    return jsonify(output)

@app.route('/places_reviews_example')
def places_reviews_example():
    """ prints out reviews of places """

    output = {}

    for key in review_data:
        row = review_data[key]
        place_id = row['place_id']
        place_name = place_data[place_id]['name']
        if place_name not in output:
            output[place_name] = []
        
        reviewer = user_data[row['commentor_user_id']]

        output[place_name].append({
            "review": row['feedback'],
            "rating": str(row['rating'] * 5) + " / 5",
            "reviewer": reviewer['first_name'] + " " + reviewer['last_name']
        })

    return jsonify(output)

# Consider adding other routes to display data for:
# - the places within the countries
# - which places are owned by which users
# - names of the owners of places with toilets

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
