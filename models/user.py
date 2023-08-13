#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """Defines the User class attributes.

    Attributes:
        email (str): An empty string representing the email of the user.
        password (str): An empty string representing the password of the user.
        first_name (str): An empty string representing the first name of the user.
        last_name (str): An empty string representing the last name of the user.
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
