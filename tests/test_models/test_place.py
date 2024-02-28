#!/usr/bin/python3
"""Test for place"""

import unittest
from models.place import Place


class test_cplace(unittest.TestCase):
    """tests place"""

    def test_place(self):
        pl = Place()
        self.assertEqual(pl.name, '')
        self.assertEqual(pl.city_id, '')
        self.assertEqual(pl.user_id, '')
        self.assertEqual(pl.description, '')
        self.assertEqual(pl.number_rooms, 0)
        self.assertEqual(pl.number_bathrooms, 0)
        self.assertEqual(pl.max_guest, 0)
        self.assertEqual(pl.price_by_night, 0)
        self.assertEqual(pl.latitude, 0.0)
        self.assertEqual(pl.longitude, 0.0)
        self.assertEqual(pl.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
