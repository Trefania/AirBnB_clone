#!/usr/bin/python3
"""
Test File for the Base Model
"""

import os
import re
import json
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test for the base model class
    """

    @classmethod
    def setUpClass(cls):
        """
        it's called to prepare the test fixture
        Setting Up my Instances.
        """
        cls.model1 = BaseModel()
        cls.model2 = BaseModel()
        cls.model3 = BaseModel()

    def test_assigning_instances(self):
        """Assigning Attributes"""
        self.model1.name = "First Model"
        self.model1.my_number = 89
        self.model2.name = "Second Model"
        self.model2.my_number = 99
        self.model3.name = "Third Model"
        self.model3.my_number = 35

    def test_models_values(self):
        """Tests Values of Models"""
        self.assertEqual([self.model1.name,self.model1.my_number],["First Model",89])
        self.assertEqual([self.model2.name, self.model2.my_number], ["Second Model", 99])
        self.assertEqual([self.model3.name, self.model3.my_number],["Third Model", 35])

    def test_datetime(self):
        """Test for current date and time"""
        pass

if __name__ == '__main__':
    unittest.main()

   
