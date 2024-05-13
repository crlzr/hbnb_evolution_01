#!/usr/bin/python3
""" initialize the storage used by models """

from data.file_storage import FileStorage

storage = FileStorage()
country_data = storage.load_from_json_file('data/country.json')
city_data = storage.load_from_json_file('data/city.json')
amenity_data = storage.load_from_json_file('data/amenity.json')
place_data = storage.load_from_json_file('data/place.json')
place_to_amenity_data = storage.load_from_json_file('data/place_to_amenity.json')
user_data = storage.load_from_json_file('data/user.json')
review_data = storage.load_from_json_file('data/review.json')
