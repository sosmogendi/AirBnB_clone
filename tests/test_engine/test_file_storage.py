#!/usr/bin/python3
"""
This module contains unit tests for the FileStorage class.
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """Set up test fixtures."""
        self.storage = FileStorage()
        self.base = BaseModel()
        self.storage.new(self.base)
        self.storage.save()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test all method."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(self.base.__class__.__name__ + '.' + self.base.id, all_objs)

    def test_new(self):
        """Test new method."""
        new_base = BaseModel()
        self.storage.new(new_base)
        self.assertIn(new_base.__class__.__name__ + '.' + new_base.id, self.storage.all())

    def test_save(self):
        """Test save method."""
        new_base = BaseModel()
        self.storage.new(new_base)
        self.storage.save()
        file_content = ""
        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_content = file.read()
        self.assertIn(new_base.__class__.__name__ + '.' + new_base.id, file_content)

    def test_reload(self):
        """Test reload method."""
        storage_copy = FileStorage()
        storage_copy.reload()
        all_objs_copy = storage_copy.all()
        self.assertIsInstance(all_objs_copy, dict)
        self.assertIn(self.base.__class__.__name__ + '.' + self.base.id, all_objs_copy)

if __name__ == '__main__':
    unittest.main()
