#!/usr/bin/python3
"""
Module: file_storage.py
"""
# import models
import json
from models.base_model import BaseModel


class FileStorage():
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "store.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__+"."+obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_to_json = {}
        for key, obj in FileStorage.__objects.items():
            key = obj.__class__.__name__+"."+obj.id
            dict_to_json[key] = obj.to_dict()
        with open(self.__file_path, 'w') as jfile:
            json.dump(dict_to_json, jfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as rfile:
                json_to_dict = json.load(rfile)

            for object_dict in json_to_dict.values():
                key = f"{object_dict['__class__']}.{object_dict['id']}"
                FileStorage.__objects.setdefault(
                        key, eval(object_dict['__class__'])(**object_dict)
                        )
            """for key, object_dict in json_to_dict.items():
                clas_name, object_id = key.split(".", 1)
                cls = getattr(models, clas_name)
                self.__objects[key] = cls(**object_dict)"""

        except FileNotFoundError:
            pass
