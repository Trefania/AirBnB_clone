#!/usr/bin/python3
"""
The Module includes a class that performs serialization
and Deserialization.
"""
import json


class FileStorage():
    """
    A Class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialization"""
        pass

    def all(self):
        """Returns the Dictionary '__objects' """
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key
        <obj class name>.id
        """
        obj_key = obj.__class__.__name__ + '.' + str(obj)
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file,
        (path: __file_path)
        """
        filename = self.__file_path
        my_obj = {}
        for k, v in self.__objects.items():
            my_obj[k] = v.to_dict()
        with open(filename, "a+") as f:
            f.write(json.dumps(my_obj))

    def reload(self):
        """Deserializes the JSON file to '__objects'
        (only if the JSON file exists)
        """
        filename = self.__file_path
        try:
            with open(filename) as f:
                my_dict = json.loads(f.read())
                for v in my_dict.values():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))
        except:
            pass
