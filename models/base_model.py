#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *argc, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary of BaseModel instance."""
        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__
        return r_dict
    
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
    