#!/usr/bin/python3
"""
    Module: base_model.py
"""
import uuid
from datetime import datetime

class base_model():
    """base model"""
    def __init__(self, id, created_at, updated_at):
        """constructor function"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[<base_model>] (<self.id>) <self.__dict__>]"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
                "id": self.id,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                }

