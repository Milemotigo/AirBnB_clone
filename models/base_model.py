#!/usr/bin/python3
"""
    Module: base_model.py
"""
import uuid
from datetime import datetime

class BaseModel():
    """base model"""
    def __init__(self, id=0, created_at=0, updated_at=0):
        """constructor function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """  """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """  """
        self.updated_at = datetime.now()

    def to_dict(self):
        """  """
        dictt = {}
        for key, val in self.__dict__.items():
            if key not in ["id", "created_at", "updated_at"]:
                dictt[key] = val
        dictt["__class__"] = self.__class__.__name__
        dictt["updated_at"] = self.updated_at.isoformat()
        dictt["id"] = self.id
        dictt["created_at"] = self.created_at.isoformat()
         
        return dictt

