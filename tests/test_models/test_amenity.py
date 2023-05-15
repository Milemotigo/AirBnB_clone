#!/usr/bin/python3
"""  """

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """  """
    user1 = User()
    def test_user(self):
        """  """
        self.assertTrue(User())

    def test_attr(self):
        """  """
        self.assertTrue(self.user1.email=='')
        self.assertTrue(self.user1.first_name=='')
