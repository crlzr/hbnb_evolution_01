#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

# from io import StringIO
# import sys
import unittest
from models.city import City
import data as data

class TestCity(unittest.TestCase):
    """Test that the models works as expected
    """

    def test_create_city(self):
        """Tests creation of City instances
        """
        # override whatever it is that was loaded in data model jsut for this test
        data.country_data = {
            "id": "d291a77f-fa95-4385-b70e-2691df246475",
            "name": "Canada",
            "created_at": 1715579247.890417,
            "updated_at": 1715579247.890417
        }

    #     c = City(name="Vancouver", country_id="d291a77f-fa95-4385-b70e-2691df246475")

    #     self.assertIsNotNone(c)

    # def test_swim_output(self):
    #     """Tests that the swim mixin works as expected
    #     """
    #     draco = Dragon()

    #     capturedOutput = StringIO()     # Create StringIO object
    #     sys.stdout = capturedOutput     # and redirect stdout.
    #     draco.swim()                    # Call unchanged function.
    #     sys.stdout = sys.__stdout__     # Reset redirect.
    #     self.assertEqual(capturedOutput.getvalue(), "The creature swims!\n")

if __name__ == '__main__':
    unittest.main()
