#!/usr/bin/python

from datetime import datetime, timezone
import uuid
import re
from app import city_data
# from models.country import Country

class City():
    """Representation of city """

    def __init__(self, *args, **kwargs):
        """ constructor """
        # super().__init__(*args, **kwargs)

        print(city_data)

        # defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__name = ""
        self.__country_id = 0

        # Only allow country_id, name.
        # Note that I'm calling the setters for these 2 attribs
        if kwargs:
            for key, value in kwargs.items():
                if key == "country_id" or key == "name":
                    setattr(self, key, value)

    @property
    def name(self):
        """Getter for private prop name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for private prop name"""

        # ensure that the value is not spaces-only and is alphabets + spaces only
        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z ]+$", value)
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid city name specified: {}".format(value))

    @property
    def country_id(self):
        """Getter for private prop country_id"""
        return self.__country_id

    @country_id.setter
    def country_id(self, value):
        """Setter for private prop country_id"""

        # TODO: ensure that the specified country actually exists before setting

        self.__country_id = value
