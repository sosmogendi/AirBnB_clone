import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class defines common attributes and methods for AirBnB objects.
    It provides serialization, deserialization, and other utilities.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Not used.
            **kwargs: Key-value pairs representing attribute values.

        Note:
            If kwargs is not empty, attribute values are set based on the dictionary.
            If kwargs is empty, id and created_at are generated as new attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary representation for serialization.

        Returns:
            dict: A dictionary containing object attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A formatted string with the object's class name and ID.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
