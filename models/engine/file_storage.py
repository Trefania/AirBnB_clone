#!/usr/bin/python3
"""
The Module includes a class that performs serialization
and Deserialization.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "Place": Place,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage():
    """
    A Class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "test.json"
    __objects = {}

    def __init__(self):
        """Initialization"""
        pass

    def all(self):
        """Returns the Dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key
        <obj class name>.id
        """
        obj_key = obj.__class__.__name__ + '.' + str(obj.id)
        # print(obj_key)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file,
        (path: __file_path)
        """
        from models.base_model import BaseModel
        # from models.user import User
        filename = FileStorage.__file_path
        my_obj = {}
        for k, v in FileStorage.__objects.items():
            my_obj[k] = v.to_dict()
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(my_obj, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'
        (only if the JSON file exists)
        """
        filename = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                my_dict = json.load(f)
                # print(my_dict)
                for k in my_dict.keys():
                    class_name = my_dict[k]["__class__"]
                    instance = my_dict[k]
                    FileStorage.__objects[k] = class_dict[class_name](
                        **instance)

        except Exception:
            pass
