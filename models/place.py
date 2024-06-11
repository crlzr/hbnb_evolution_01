#!/usr/bin/python

from datetime import datetime
import uuid
import re
from data import user_data, city_data

class Place():
    """Representation of Places """

    def __init__(self, *args, **kwargs):
        """ constructor """

        # defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__host_user_id = ""
        self.__name = ""
        self.__city_id = ""
        self.__description = ""
        self.__address = ""
        self.__latitude = 0.0
        self.__longitude = 0.0
        self.__number_of_rooms = 0
        self.__bathrooms = 0
        self.__price_per_night = 0.0
        self.__max_guests = 0


        allowed_attributes = ["host_user_id", "name", "city_id", "description", "address",
                              "latitude", "longitude", "number_of_rooms", "bathrooms",
                              "price_per_night", "max_guests"]

        # Allow all of the above.
        # Note that setattr will call the setters for all of the above
        if kwargs:
            for key, value in kwargs.items():
                if key in allowed_attributes:
                    setattr(self, key, value)

    @property
    def host_user_id(self):
        """Getter for private prop host_user_id"""
        return self.__host_user_id

    @host_user_id.setter
    def host_user_id(self, value):
    # ensure that the specified host_user id actually exists before setting
        if user_data.get(value) is not None:
            self.__host_user_id = value
        else:
            raise ValueError("Invalid host_user_id specified: {}".format(value))

    @property
    def name(self):
        """Getter for private prop name"""
        return self.__name


    @name.setter
    def name(self, value):
        """Setter for private prop name"""

        # ensure that the value is not spaces-only and is alphabets + spaces only
        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z \-]+$", value)
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid city name specified: {}".format(value))


    @property
    def city_id(self):
        """Getter for private prop city_id"""
        return self.__city_id

    @city_id.setter
    def city_id(self, value):
    # ensure that the specified city id actually exists before setting
        if city_data.get(value) is not None:
            self.__city_id = value
        else:
            raise ValueError("Invalid city_id specified: {}".format(value))

    @property
    def description(self):
        """Getter for private prop description"""
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value
        else:
            raise TypeError("String must be an str. Got {}".format(type(value)))

    @property
    def address(self):
        """Getter for private prop address"""
        return self.__address

    @address.setter
    def address(self, value):
        """Setter for private prop address"""

    # ensure that the value is not spaces-only and is alphabets + spaces only
        is_valid_address = len(value.strip()) > 0 and re.search("^[a-zA-Z0-9 \-]+$", value)
        if is_valid_address:
            self.__address = value
        else:
            raise ValueError("Invalid address specified: {}".format(value))

    @property
    def latitude(self):
        """Getter for private prop latitude"""
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if re.search("^[\-]?[0-9]+\.[0-9]+$", value):
            self.__latitude = value
        else:
            raise ValueError("Invalid latitude specified: {}".format(value))


    @property
    def longitude(self):
        """Getter for private prop longitude"""
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if re.search("^[\-]?[0-9]+\.[0-9]+$", value):
            self.__longitude = value
        else:
            raise ValueError("Invalid longitude specified: {}".format(value))

    @property
    def number_of_rooms(self):
        """Getter for private prop number_of_rooms"""
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        if isinstance(value, int) and value >= 0:
            self.__number_of_rooms = value
        else:
            raise TypeError("Number of rooms must be an int. Got {}".format(type(value)))

    @property
    def bathrooms(self):
        """Getter for private prop bathrooms"""
        return self.__bathrooms

    @bathrooms.setter
    def bathrooms(self, value):
        if isinstance(value, int) and value >= 0:
            self.__bathrooms = value
        else:
            raise TypeError("Bathrooms must be an int. Got {}".format(type(value)))

    @property
    def price_per_night(self):
        """Getter for private prop price_per_night"""
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if isinstance(value, float) and value >= 0:
            self.__price_per_night = value
        else:
            raise TypeError("Price per night must be a float. Got {}".format(type(value)))

    @property
    def max_guests(self):
        """Getter for private prop max guests"""
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value):
        if isinstance(value, int) and value >= 0:
            self.__max_guests = value
        else:
            raise TypeError("Max guests must be an int. Got {}".format(type(value)))
