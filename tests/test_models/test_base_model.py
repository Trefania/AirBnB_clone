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
        self.assertEqual([self.model1.name, self.model1.my_number], [
                         "First Model", 89])
        self.assertEqual([self.model2.name, self.model2.my_number], [
                         "Second Model", 99])
        self.assertEqual([self.model3.name, self.model3.my_number], [
                         "Third Model", 35])

    def test_id_type(self):
        """Test for id type"""
        self.assertTrue(type(self.model1.id), str)
        self.assertTrue(type(self.model2.id), str)
        self.assertTrue(type(self.model3.id), str)

    def test_created_at_type(self):
        """Test for created_at type"""
        self.assertTrue(type(self.model1.created_at), datetime)
        self.assertTrue(type(self.model2.created_at), datetime)
        self.assertTrue(type(self.model3.created_at), datetime)

    def test_updated_at_type(self):
        """Test for updated_at type"""
        self.assertTrue(type(self.model1.updated_at), datetime)
        self.assertTrue(type(self.model2.updated_at), datetime)
        self.assertTrue(type(self.model3.updated_at), datetime)

    def test_kwargs(self):
        """testing kwargs and args"""
        model1_dict = self.model1.to_dict()
        model2_dict = self.model2.to_dict()
        model3_dict = self.model3.to_dict()

        new_model1 = BaseModel(**model1_dict)
        new_model2 = BaseModel(**model2_dict)
        new_model3 = BaseModel(**model3_dict)

        self.assertEqual
        (type(new_model1.created_at), "<class 'datetime.datetime'>")
        self.assertEqual
        (type(new_model2.created_at), "<class 'datetime.datetime'>")
        self.assertEqual
        (type(new_model3.created_at), "<class 'datetime.datetime'>")


if __name__ == '__main__':
    unittest.main()
