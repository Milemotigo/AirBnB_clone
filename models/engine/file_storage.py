#!/usr/bin/python3
"""
Module: file_storage.py
"""
import json

class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "store.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__+"."+obj.id
        self.__object[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_to_json = {}
        for key, obj in self.__objects.items():
            dict_to_json[key] = obj.to_dict()
        with open(self.__file_path, 'w') as jfile:
            json.dumps(dict_to_json, jfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            json_to_dict = {}

        except FileNotFoundError:
            pass
