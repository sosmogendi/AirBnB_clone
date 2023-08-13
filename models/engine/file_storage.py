#!/usr/bin/python3
import json

class FileStorage:
    """
    This class defines the FileStorage that serializes and deserializes
    instances to and from JSON files. It manages the storage and retrieval
    of objects in a JSON format file.
    
    Attributes:
        __file_path (str): The path to the JSON file for storage.
        __objects (dict): A dictionary storing all serialized objects by their
                          unique keys in the format "<class name>.<object id>".
                          
    Methods:
        all(self): Returns the dictionary of all serialized objects.
        new(self, obj): Adds a new object to the dictionary of serialized objects.
        save(self): Serializes and saves all objects in the dictionary to the JSON file.
        reload(self): Deserializes and loads objects from the JSON file to the dictionary.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all serialized objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of serialized objects.
        
        Args:
            obj: The object to be serialized and stored.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes and saves all objects in the dictionary to the JSON file."""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes and loads objects from the JSON file to the dictionary."""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                from models.base_model import BaseModel
                # Import other classes here
                # Deserialize instances from JSON data
                for key, value in self.__objects.items():
                    class_name = value['__class__']
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
