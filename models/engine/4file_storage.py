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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__+"."+obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_to_json = {}
        for key, obj in FileStorage.__objects.items():
            key = f"{obj.__class__.__name__}.{obj.id}"
            dict_to_json.setdefault(key, obj.to_dict())

        with open(self.__file_path, 'w') as jfile:
            json.dump(dict_to_json, jfile, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as rfile:
                json_to_dict = json.load(rfile)

            for ob_dict in json_to_dict.values():
                class_name, obj_id = ob_dict['__class__'].split(".", 1)
                cls = globals()[class_name]
                key = f"{class_name}.{obj_id}"
                FileStorage.__objects[key] = cls(**ob_dict)
                """key = f"{ob_dict['__class__']}.{ob_dict['id']}"
                FileStorage.__objects.setdefault(key, eval(ob_dict['__class__'])(**ob_dict))"""

        except FileNotFoundError as err:
            pass
