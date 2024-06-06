#!/usr/bin/python

from datetime import datetime
import uuid
import re
from data import user_data

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
        self.__latitude = ""
        self.__longitude = ""
        self.__number_of_rooms = ""
        self.__bathrooms = ""
        self.__price_per_night = ""
        self.__max_guests = ""


        allowed_attributes = ["host_user_id", "name", "city_id", "description", "address",
                              "latitude", "longitute", "number_of_rooms", "bathrooms",
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
    #Code here

    @property
    def description(self):
        """Getter for private prop description"""
        return self.__description

    @description.setter
    #Code here

    @property
    def address(self):
        """Getter for private prop address"""
        return self.__address

    @address.setter
    #Code here

    @property
    def latitude(self):
        """Getter for private prop latitude"""
        return self.__latitude

    @latitude.setter
    #Code here

    @property
    def longitude(self):
        """Getter for private prop longitude"""
        return self.__longitude

    @longitude.setter
    #Code here

    @property
    def number_of_rooms(self):
        """Getter for private prop number_of_rooms"""
        return self.__number_of_rooms

    @number_of_rooms.setter
    #Code here

    @property
    def bathrooms(self):
        """Getter for private prop bathrooms"""
        return self.__bathrooms

    @bathrooms.setter
    #Code here

    @property
    def price_per_night(self):
        """Getter for private prop price_per_night"""
        return self.__price_per_night

    @price_per_night.setter
    #Code here

    @property
    def max_guests(self):
        """Getter for private prop max guests"""
        return self.__max_guests

    @max_guests.setter
    #Code here



