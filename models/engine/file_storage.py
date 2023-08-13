#!/usr/bin/python3
"""
This module defines the FileStorage class that serializes and deserializes
instances to and from JSON files.
"""

import json
import os.path
from datetime import datetime
from models.base_model import BaseModel

class FileStorage:
    """
    This class manages serialization and deserialization of instances to/from JSON.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                serialized = json.load(file)
                for key, value in serialized.items():
                    cls_name = value['__class__']
                    obj = globals()[cls_name](**value)
                    self.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle the case where the file is empty or not valid JSON
            pass

