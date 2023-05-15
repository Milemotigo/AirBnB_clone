#!/usr/bin/python3
"""Unittest for base_model file"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """   """
    test = BaseModel(self)
    def test_basemodel(self):
        """  """
        self.assertTrue(BaseModel())

    def test_user(self):
        """  """
        self.assertTrue(BaseModel)
        self.assertTrue(isinstance(self.User, BaseModel))
