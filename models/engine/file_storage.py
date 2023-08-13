#!/usr/bin/python3
"""
file_storage.py module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    FileStorage class:
    ------------------
    This class handles the serialization and deserialization of objects to and
    from JSON files. It manages the storage and retrieval of objects in a
    dictionary format.

    Attributes:
        __file_path (str): The path to the JSON file for storage.
        __objects (dict): A dictionary storing all serialized objects by their
                          unique keys in the format "<class name>.<object id>".

    Methods:
        all(self): Returns the dictionary containing all serialized objects.
        new(self, obj): Adds a new object to the dictionary of serialized objects.
        save(self): Serializes and saves all objects in the dictionary to the JSON file.
        reload(self): Deserializes and loads objects from the JSON file to the dictionary.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj: The object to be serialized and stored.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and saves all objects in the dictionary to the JSON file.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        Deserializes and loads objects from the JSON file to the dictionary.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
