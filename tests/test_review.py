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

    def test_feedback_not_string(self):
        """
        Tests if feedback is not string
        """
        test_error = ""
        try:
            Reviews(commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    place_id="cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
                    feedback=999999999,
                    rating=4)
        except Exception as e:
            test_error = e

        self.assertIsInstance(test_error, TypeError)

    def test_rating_not_int(self):
        """
        Tests if rating is not int
        """
        test_error = ""
        try:
            Reviews(commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    place_id="cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
                    feedback="If I could give 0 stars, I would",
                    rating="If I could give 0 stars, I would")
        except Exception as e:
            test_error = e

        self.assertIsInstance(test_error, TypeError)

    def test_rating_wrong_value(self):
        """
        Tests if rating is wrong value (< 1 or > 5)
        """
        test_error = ""
        try:
            Reviews(commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    place_id="cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
                    feedback="If I could give 0 stars, I would",
                    rating=0)
        except Exception as e:
            test_error = e

        self.assertIsInstance(test_error, ValueError)




if __name__ == '__main__':
    unittest.main()
