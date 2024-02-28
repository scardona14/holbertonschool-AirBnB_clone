#!/usr/bin/python3
"""Test for amenity"""

import unittest
from models.amenity import Amenity


class test_camenity(unittest.TestCase):
    """tests amenity"""

    def test_amenity(self):
        am = Amenity()
        self.assertEqual(am.name, "")


if __name__ == '__main__':
    unittest.main()
