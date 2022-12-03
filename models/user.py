from models.base_model import BaseModel
# !/usr/bin/python3
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
