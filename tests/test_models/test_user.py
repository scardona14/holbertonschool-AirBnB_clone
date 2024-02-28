#!/usr/bin/python3
"""Testerino"""

import unittest
from models.user import User


class test_cuser(unittest.TestCase):
    def test_user(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertEqual(u.password, "")

if __name__ == '__main__':
        unittest.main()
