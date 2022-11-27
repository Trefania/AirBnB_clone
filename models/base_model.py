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

    def __init__(self, *args, **kwargs):
        """Initialization of the Class
        Args:
            args - not used
            kwargs - keywords arguments/ dictionary.
        """
        from models import storage

        # Used a datetime format
        format_data = "%Y-%m-%dT%H:%M:%S.%f"
        # If a keyword argument is passed;
        if kwargs:
            # Iterate through the keyword argument items.
            for k, v in kwargs.items():
                # Aslong as the keys aren't the __class__ key
                if not k == "__class__":
                    # If the key equals id.
                    if k == "id":
                        #  Assign the dict key to the value.
                        self.__dict__[k] = str(v)
                    # If key equals created at or updated at
                    if k == "created_at" or k == "updated_at":
                        # Assign the dict key to the datetime time of its value.
                        self.__dict__[k] = dt.strptime(v, format_data)
                    else:
                        # Sets the attributes to their values.
                        setattr(self, k, v)
        # Else if no key word args
        else:
            # Assigns the various attributes to their various values.
            # The ID has a value of the universal unique id 4
            self.id = str(uuid.uuid4())
            # Created at has value of the current time.
            self.created_at = dt.now()
            # Updated at has value of the current time.
            self.updated_at = dt.now()
            # Calls the new function of the storage.
            storage.new(self)

    def __str__(self):
        """String Representation"""
        return "[{}], ({}), {}".format(self.
                                       __class__.__name__, self.id, self.
                                       __dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at'
        with the current datetime
        """
        from models import storage

        # Updates the updated at attribute to the time of new update
        self.updated_at = dt.now()
        # Calls the save function to save attrs updated.
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        # Initialised an empty dictionary
        our_dict = {}
        # Assigns the __class__ to the class name.
        our_dict["__class__"] = self.__class__.__names__
        # iterates through the self dictionary items
        for k, v in self.__dict__.items():
            # If key equals created at.
            if k == "created_at":
                # Converts the key value to the datetime format declared earlier
                our_dict[k] = v.isoformat()
            # If Key equals updated at
            elif k == "updated_at":
                # Converts the key value to the datetime format.
                our_dict[k] = v.isoformat()
            else:
                # Assings the other keys to their values.
                our_dict[k] = v
        # Returns the dictionarys.
        return our_dict
