#!/usr/bin/python3
"""Test for state"""

import unittest
from models.state import State


class test_cstate(unittest.TestCase):
    def test_state(self):
        st = State()
        self.assertEqual(st.name, "")


if __name__ == '__main__':
    unittest.main()
