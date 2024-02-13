#!/usr/bin/python3
"""Defines the FileStorage"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r',encoding="utf-8") as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj_instance = cls(**value)
                    self.new(obj_instance)
        except FileNotFoundError:
            pass


