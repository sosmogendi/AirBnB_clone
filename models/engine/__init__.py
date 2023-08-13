#!/usr/bin/python3
"""
This module initializes the engine package.
"""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()
# Load data from JSON file into storage
storage.reload()
