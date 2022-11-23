#!/usr/bin/python3
"""Initialization File of Package.
Creates a unique FileStorage instance for the Application.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
