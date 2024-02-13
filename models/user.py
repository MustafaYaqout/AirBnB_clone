#!/usr/bin/python3
""" this module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""