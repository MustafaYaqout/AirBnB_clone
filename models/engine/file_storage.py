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
            """Deserialize the JSON file __file_path to __objects, if it exists."""
            try:
                with open(FileStorage.__file_path) as f:
                        objdict = json.load(f)
                        for o in objdict.values():
                            cls_name = o["_class_"]
                            del o["_class_"]
                            self.new(eval(cls_name)(**o))
            except FileNotFoundError:
                    return

