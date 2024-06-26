#!/usr/bin/python3
""" initialize the storage used by models """

import os
from data.file_storage import FileStorage

storage = FileStorage()

# check for TESTING=1 from command line
# command to use: TESTING=1 python3 -m unittest discover
is_testing = "TESTING" in os.environ and os.environ['TESTING'] == "1"

if is_testing:
    country_data = storage.load_model_data('data/country_testing.json')
    city_data = storage.load_model_data('data/city_testing.json')
    amenity_data = storage.load_model_data('data/amenity_testing.json')
    place_data = storage.load_model_data('data/place_testing.json')
    user_data = storage.load_model_data('data/user_testing.json')
    review_data = storage.load_model_data('data/review_testing.json')
    place_to_amenity_data = storage.load_many_to_many_data('data/place_to_amenity_testing.json')
else:
    country_data = storage.load_model_data('data/country.json')
    city_data = storage.load_model_data('data/city.json')
    amenity_data = storage.load_model_data('data/amenity.json')
    place_data = storage.load_model_data('data/place.json')
    user_data = storage.load_model_data('data/user.json')
    review_data = storage.load_model_data('data/review.json')
    place_to_amenity_data = storage.load_many_to_many_data('data/place_to_amenity.json')
