#!/usr/bin/python3
"""
Module: file_storage.py
"""
import models
import json


class FileStorage():
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "store.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__+"."+obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_to_json = {}
        for key, obj in self.__objects.items():
            dict_to_json[key] = obj.to_dict()
        with open(self.__file_path, 'w') as jfile:
            json.dump(dict_to_json, jfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as rfile:
                json_to_dict = json.load(rfile)

            for key, object_dict in json_to_dict.items():
                clas_name, object_id = key.split(".", 1)
                cls = getattr(models, clas_name)
                # cls = globals()[clas_name]
                self.__objects[key] = cls(**object_dict)

        except FileNotFoundError:
            pass
