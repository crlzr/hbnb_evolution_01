#!/usr/bin/python /// STILL TO DO

from datetime import datetime
import uuid
import re
from data import country_data

class Amenity():
    """Representation of Amenity """

    def __init__(self, *args, **kwargs):
        """ constructor """
        # super().__init__(*args, **kwargs)

        # defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__name = ""

        # Only allow amenity name.
        # Note that setattr will call the setter for this attribute
        if kwargs:
            for key, value in kwargs.items():
                if key == "name":
                    setattr(self, key, value)

    @property
    def name(self):
        """Getter for private name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for private name"""

        # ensure that the value is not spaces-only and is alphabets + spaces only
        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z ]+$", value)
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid amenity name specified: {}".format(value))
