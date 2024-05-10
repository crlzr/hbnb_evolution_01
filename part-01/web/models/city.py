#!/usr/bin/python

from datetime import datetime, timezone
import uuid

class City():
    """Representation of city """

    def __init__(self, *args, **kwargs):
        """ constructor """
        # super().__init__(*args, **kwargs)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        # self.name = ""
        # self.country_id = 0

        # Only allow country_id, name. Others are filtered / set automatically
        if kwargs:
            for key, value in kwargs.items():
                if key == "country_id" or key == "name":
                    setattr(self, key, value)
                else:
                    print("Key '{}' ignored.".format(key))
