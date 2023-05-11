#!/usr/bin/python3
"""
    Module: base_model.py
"""
import uuid
from datetime import datetime

class base_model():
    """base model"""
    def __init__(self, id=0, created_at=0, updated_at=0):
        """constructor function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """  """
        return f"{[self.__class__.__name__]} {(self.id}) {self.__dict__}"

    def save(self):
        """  """
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
                "id": self.id,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                }

