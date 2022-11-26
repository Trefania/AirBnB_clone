#!/usr/bin/python3
"""
A Module with City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
