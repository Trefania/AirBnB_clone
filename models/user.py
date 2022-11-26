from models.base_model import BaseModel
b  # !/usr/bin/python3
"""User Class Module that inherits from BaseModel"""


class User(BaseModel):
    """
    User Class that inherits from BaseModel
    Public Class Attributes;
            -> email
            -> password
            -> first_name
            -> last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self):
    #     """Initialization"""
    #     from models import storage
    #     super.__init__()
    #     storage.new(self)

    # def save(self):
    #     """Saves all User Instances Created."""
    #     from models import storage
    #     storage.save()
