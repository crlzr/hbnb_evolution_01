#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

# from io import StringIO
# import sys
import os
import unittest
from models.city import City
import data as data

class TestCity(unittest.TestCase):
    """Test that the models works as expected
    """

    def test_create_city(self):
        """Tests creation of City instances
        """
        # Note that this test only works if the test country data is loaded
        # don't forget to include the TESTING = 1 flag at the command line
        # TESTING=1 python3 -m unittest discover
        c = City(name="Vancouver", country_id="d291a77f-fa95-4385-b70e-2691df246475")

        self.assertIsNotNone(c)

    # TODO: add more tests


if __name__ == '__main__':
    unittest.main()
