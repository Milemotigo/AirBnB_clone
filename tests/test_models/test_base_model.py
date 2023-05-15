#!/usr/bin/python3
"""Unittest for base_model file"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """   """
    test = BaseModel()
    def test_BaseModel(self):
        """  """
        self.assertTrue(BaseModel())

    def test_User(self):
        """  """
        self.assertTrue(BaseModel)
        self.assertTrue(isinstance(self.User, BaseModel))
