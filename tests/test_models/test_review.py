#!/usr/bin/python3
"""Test for review"""

import unittest
from models.review import Review


class test_creview(unittest.TestCase):
    """tests review"""
    def test_review(self):
        rv = Review()
        self.assertEqual(rv.place_id, "")
        self.assertEqual(rv.user_id, "")
        self.assertEqual(rv.text, "")


if __name__ == '__main__':
    unittest.main()
