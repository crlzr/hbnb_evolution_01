#!/usr/bin/python

import json

class FileStorage():
    """ Class for reading from files """

    def load_from_json_file(self, filename):
        """ Load JSON data from file and returns as dictionary """

        data = {}
        try:
            with open(filename, 'r') as f:
                rows = json.load(f)
            for key in rows:
                data[key] = rows[key]
        except:
            raise ValueError("Something happened")

        # The data at this point is not directly usable. It needs to be cleaned up
        data = self.reorganise_data(data)

        return data

    def reorganise_data(self, data):
        """ Parse and reorganise the data so that the id is the key """
        output = {}

        # To make it easier to look for certain ids in the loaded data
        # we are going to rebuild the dictionary so that the row id (uuid)
        # is also the key for the record

        for key in data:
            # print("Rebuilding loaded data for {}...".format(key))
            # print(data[key])
            for row in data[key]:
                output[row['id']] = row

        return output
