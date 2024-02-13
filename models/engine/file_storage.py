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
        FileStorage.__objects["{}.{}".format(obj_name, obj)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
            """Deserialize the JSON file __file_path to __objects, if it exists."""
            try:
                with open(FileStorage.__file_path) as file:
                    object_json = json.load(file)
                    for obj in object_json.values():
                        class_name = obj['__class__']
                        del class_name
                        self.new(obj)

            except FileNotFoundError:
                return

