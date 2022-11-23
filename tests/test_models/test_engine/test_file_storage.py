#!/usr/bin/python3
"""Unittest module for the file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test Cases for the class."""

    def setUp(self):
        """Sets up class"""
        pass

    def resetStorage(self):
        """Resets Filestorage data"""
        FileStorage.__objects = {}
        if os.path.isfile(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)
