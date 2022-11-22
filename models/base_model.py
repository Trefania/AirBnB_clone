#!/usr/bin/python3
"""
The base_model module contains the BaseModel Class
"""
import uuid
from datetime import datetime as dt


class BaseModel():
    """
    The BaseModel Class that defines all common attributes
    methods for other classes.
    Args:
        public instance attributes:
            id - string using uuid4.
            created_at - datetime when an instance is created.
            updated_at - datetime when an instance is changed.
        public instance methods:
            save - updates the current datetime of updated_at
            to_dict - returns a dictionary containing all key/values
                of __dict__ of the instance.
    """

    def __init__(self):
        """Initialization of the Class"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        """String Representation"""
        return "[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = dt.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        our_dict = {}
        our_dict["__class__"] = self.__class__.__name__
        for k,v in self.__dict__.items():
            if k == "created_at":
                our_dict[k] = v.isoformat()
            elif k == "updated_at":
                our_dict[k] = v.isoformat()
            else:
                our_dict[k] = v
        return our_dict
