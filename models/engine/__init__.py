#!/usr/bin/python3
"""
This module initializes the engine package.
"""

from models.engine.file_storage import FileStorage

# Create a storage instance
storage = FileStorage()

# Load the stored data from file
storage.reload()
