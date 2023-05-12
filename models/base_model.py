#!/usr/bin/python3
"""
    Module: base_model.py
"""
import uuid
from datetime import datetime, date
import models

class BaseModel():
    """base model"""
    def __init__(self, *args, **kwargs):
        """constructor function"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key not in ["created_at", "updated_at"]:
                    if key != "__class__":
                        setattr(self, key, val)
                else:
                     setattr(self, key, datetime.fromisoformat(val))

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictt = {}
        for key, val in self.__dict__.items():
            if key not in ["created_at", "updated_at"]:
                dictt[key] = val
        dictt["__class__"] = self.__class__.__name__
        dictt["created_at"] = self.updated_at.isoformat()
        #dictt["id"] = self.id
        dictt["updated_at"] = self.created_at.isoformat()
        return dictt

