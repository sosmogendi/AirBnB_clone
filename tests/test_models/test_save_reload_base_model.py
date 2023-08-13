#!/usr/bin/python3

"""
This script demonstrates the process of reloading objects from storage,
printing reloaded objects, and creating a new object using the BaseModel class.
"""

from models import storage
from models.base_model import BaseModel

# Reload all objects from storage
all_objs = storage.all()

# Print header for reloaded objects
print("-- Reloaded objects --")

# Iterate through reloaded objects and print them
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Print header for creating a new object
print("-- Create a new object --")

# Create a new instance of BaseModel
my_model = BaseModel()

# Set attributes for the new instance
my_model.name = "My_First_Model"
my_model.my_number = 89

# Save the new instance to storage
my_model.save()

# Print the details of the new instance
print(my_model)
