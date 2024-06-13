#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

import unittest
from models.review import Reviews

class TestReview(unittest.TestCase):
    """Test that the models works as expected
    """

    def test_create_review(self):
        """Tests creation of Review instances """

        # don't forget to include the TESTING = 1 flag at the command line
        # type in the terminal: TESTING=1 python3 -m unittest discover
        r = Reviews(commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    place_id="cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
                    feedback="If I could give 0 stars, I would",
                    rating=4)

        self.assertIsNotNone(r)

    def feedback_is_string(self):
        """
        Tests if feedback is wrong type
        """
        test_error = ""
        try:
            Reviews(commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    place_id="cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
                    feedback=999999999,
                    rating=4)
        except TypeError as e:
            test_error = e

        self.assertIsInstance(test_error, TypeError)




if __name__ == '__main__':
    unittest.main()
