#!/usr/bin/python3
"""Initialization File of Package.
Creates a unique FileStorage instance for the Application.
"""
from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
