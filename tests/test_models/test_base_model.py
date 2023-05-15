#!/usr/bin/python3
"""Unittest for base_model file"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """   """
    user0 = BaseModel()
    user1 = User()
    def test_BaseModel(self):
        """  """
        self.assertTrue(BaseModel())

    def test_User(self):
        """  """
        self.assertTrue:(User())
        self.assertTrue(isinstance(self.user1.email, str))

    def test_attribuites(self):
        """  """
        self.assertTrue(hasattr(self.user0, "id"))

    def test_methods(self):
        """  """
        self.assertTrue(hasattr(self.user0, "save"))
