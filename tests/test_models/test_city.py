#!/usr/bin/python3
"""Testerino"""

import unittest
from models.city import City


class test_ccity(unittest.TestCase):
    """tests city"""

    def test_city(self):
        c1 = City()
        self.assertEqual(c1.state_id, "")
        self.assertEqual(c1.name, "")

if __name__ == '__main__':
        unittest.main()
