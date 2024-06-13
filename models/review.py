#!/usr/bin/python

from datetime import datetime
import uuid
from data import user_data, place_data


class Reviews():
    """Representation of Reviews """

    def __init__(self, *args, **kwargs):
        """ constructor """

        # defaults
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__commentor_user_id = ""
        self.__place_id = ""
        self.__feedback = ""
        self.__rating = 1

        allowed_attributes = ["commentor_user_id", "place_id", "feedback", "rating"]

        # Only allow country_id, name.
        # Note that setattr will call the setters for these 2 attribs
        if kwargs:
            for key, value in kwargs.items():
                if key in allowed_attributes:
                    setattr(self, key, value)

    @property
    def commentor_user_id(self):
        """Getter for private commentor user id"""
        return self.__commentor_user_id

    @commentor_user_id.setter
    def commentor_user_id(self, value):
    # ensure that the specified commentor_user id actually exists before setting
        if user_data.get(value) is not None:
            self.__commentor_user_id = value
        else:
            raise ValueError("Invalid commentor_user_id specified: {}".format(value))

    @property
    def place_id(self):
        """Getter for private place id"""
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
    # ensure that the specified place_id actually exists before setting
        if place_data.get(value) is not None:
            self.__place_id = value
        else:
            raise ValueError("Invalid place id specified: {}".format(value))

    @property
    def feedback(self):
        """Getter for private feedback"""
        return self.__feedback

    @feedback.setter
    def feedback(self, value):
        if isinstance(value, str):
            self.__feedback = value
        else:
            raise TypeError("Feedback must be a string. {}".format(value))

    @property
    def rating(self):
        """Getter for private rating"""
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an int between 1.0 and 5.0: {}".format(value))
        if value < 1 or value > 5:
            raise ValueError("Rating must be an int between 1.0 and 5.0: {}".format(value))

        self.__rating = value

