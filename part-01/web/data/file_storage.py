#!/usr/bin/python

import json

class FileStorage():
    """ Class for reading from files """

    def load_from_json_file(self, filename):
        """ Load JSON data from file and returns as dictionary """

        output = {}
        try:
            with open(filename, 'r') as f:
                rows = json.load(f)
            for key in rows:
                output[key] = rows[key]
        except:
            raise ValueError("Something happened")

        return output
