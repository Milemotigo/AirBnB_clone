#!/usr/bin/python3
"""  """

import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """  """
    user1 = Place()
    def test_user(self):
        """  """
        self.assertTrue(Place())

    def test_attr(self):
        """  """
        self.assertTrue(self.user1.email=='')
        self.assertTrue(self.user1.first_name=='')
