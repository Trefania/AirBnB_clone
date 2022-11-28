#!/usr/bin/python3
"""Unittest module for the file storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
import os
import json
from models.engine.file_storage import class_dict


class TestFileStorage(unittest.TestCase):
    """Test Cases for the class."""

    def setUp(self):
        """Sets up class"""
        pass

    def resetStorage(self):
        """Resets Filestorage data"""
        FileStorage._FileStorage__objects = {}
        # name mangling  for accessing our private attribute
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def tearDown(self):
        self.resetStorage()
        pass
    """
    - Storage Type
    - Init with args
    - Init without values
    - Reload test func
        classes reload
            - many args
            - less args
    - All test
        - many args
        - less args
    - New test
        - many args
        - less args
    - Save test
        - many args
        - less args
    """
    def test_for_storage_type(self):
        """ testing the type of file_storage """
        self.assertEqual(type(storage).__name__, "FileStorage")
    
    def test_init_with_args(self):
        """Testing the FileStorage init with args"""
        with self.assertRaises(TypeError):
            FileStorage(1,2,3,4,5,6,7)
    
    def test_init_without_values(self):
        """Testing the file storage without values"""
        with self.assertRaises(TypeError):
            FileStorage.__init__()
    
    def class_all_test(self, cls_name):
        """The all() test for classes"""
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        obj = class_dict[cls_name]()
        storage.new(obj)
        key = f"{cls_name}.{obj.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)
        

    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.class_all_test("BaseModel")
    
    def test_all_user(self):
        """Tests all() method for Users."""
        self.class_all_test("User")

    def test_all_state(self):
        """Test all() methods for State"""
        self.class_all_test("State")

    def test_all_city(self):
        """Test all() methods for city"""
        self.class_all_test("City")
    
    def test_all_review(self):
        """Test all() methods for review"""
        self.class_all_test("Review")

    def test_all_amenity(self):
        """Test all() methods for Amenity"""
        self.class_all_test("Amenity")
    
    def test_all_place(self):
        """Test all() methods for State"""
        self.class_all_test("Place")

    def all_many_args(self, cls_name):
        """All test all() method with many objects for cls_name."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        keys = class_dict[cls_name]
        objs = [keys() for i in range(50)]
        [storage.new(objs) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for ob in objs:
            k = f"{type(ob).__name__}.{ob.id}"
            self.assertTrue(k in storage.all())
            self.assertEqual(storage.all()[k], ob)
    
    def test_all_many_args_basemodel(self):
        """Test all() method for Basemodel
        with many args.
        """
        self.all_many_args("BaseModel")

    def test_all_many_args_user(self):
        """Test all() method for user
        with many args.
        """
        self.all_many_args("User")

    def test_all_many_args_state(self):
        """Test all() method for State
        with many args.
        """
        self.all_many_args("State")

    def test_all_many_args_city(self):
        """Test all() method for City
        with many args.
        """
        self.all_many_args("City")

    def test_all_many_args_amenity(self):
        """Test all() method for Amenity
        with many args.
        """
        self.all_many_args("Amenity")

    def test_all_many_args_place(self):
        """Test all() method for Place
        with many args.
        """
        self.all_many_args("Place")

    def test_all_many_args_review(self):
        """Test all() method for Review
        with many args.
        """
        self.all_many_args("Review")
        
    def test_all_without_args(self):
        """Test all() without arguements"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.all()

    def test_all_with_args(self):
        """Test all() with arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.all(self, 2, 3, 4, 5)

    def class_new_test(self, cls_name):
        """class test new() method for classname"""
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        keys = class_dict[cls_name]
        objs = keys()
        storage.new(objs)
        k = f"{type(objs).__name__}.{objs.id}"
        self.assertTrue(k in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[k], objs)

    def test_new_basemodel(self):
        """Test new() method for BaseModel"""
        self.class_new_test("BaseModel")

    def test_new_user(self):
        """Test new() method for User"""
        self.class_new_test("User")

    def test_new_state(self):
        """Test new() method for State"""
        self.class_new_test("State")
        
    def test_new_city(self):
        """Test new() method for City"""
        self.class_new_test("City")
        
    def test_new_place(self):
        """Test new() method for Place"""
        self.class_new_test("Place")

    def test_new_review(self):
        """Test new() method for Review"""
        self.class_new_test("Review")
        
    def test_new_amenity(self):
        """Test new() method for Amenity"""
        self.class_new_test("Amenity")

    def test_new_without_args(self):
        """Test new() without arguements"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.new()

    def test_new_with_args(self):
        """Test new() with arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.new(self, 2, 3, 4, 5)


    def class_save_test(self, cls_name):
        """Class test save() method for classname"""
        self.resetStorage()
        key = class_dict[cls_name]
        objs = key()
        storage.new(objs)
        k = f"{type(objs).__name__}.{objs.id}"
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {k: objs.to_dict()}
        path = FileStorage._FileStorage__file_path
        with open(path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()),len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.class_save_test("BaseModel")

    def test_save_user(self):
        """Tests save() method for User"""
        self.class_save_test("User")

    def test_save_state(self):
        """Tests save() method for State"""
        self.class_save_test("State")
    
    def test_save_review(self):
        """Tests save() method for Review"""
        self.class_save_test("Review")
    
    def test_save_city(self):
        """Tests save() method for City"""
        self.class_save_test("City")

    def test_save_place(self):
        """Tests save() method for Place"""
        self.class_save_test("Place")

    def test_save_amenity(self):
        """Tests save() method for Amenity"""
        self.class_save_test("Amenity")

    def test_save_without_args(self):
        """Test save() without arguements"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.save()

    def test_save_with_args(self):
        """Test save() with arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.save(self, 2, 3, 4, 5)

    def class_reload_test(self, cls_name):
        """class test reload() for classname"""
        self.resetStorage()
        self.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        key = class_dict[cls_name]
        objs = key()
        storage.new(objs)
        k = f"{type(objs).__name__}.{objs.id}"
        storage.save()
        storage.reload()
        self.assertEqual(objs.to_dict(), storage.all()[k].to_dict())

    def test_reload_basemodel(self):
        """Tests reload() method for BaseModel"""
        self.class_reload_test("BaseModel")

    def test_reload_user(self):
        """Tests reload() method for User"""
        self.class_reload_test("User")
        
    def test_reload_place(self):
        """Tests reload() method for Place"""
        self.class_reload_test("Place")

    def test_reload_city(self):
        """Tests reload() method for City"""
        self.class_reload_test("City")

    def test_reload_review(self):
        """Tests reload() method for Review"""
        self.class_reload_test("Review")
    
    def test_reload_state(self):
        """Tests reload() method for State"""
        self.class_reload_test("State")
    

    def test_reload_amenity(self):
        """Tests reload() method for Amenity"""
        self.class_reload_test("Amenity")

    def test_reload_without_args(self):
        """Test reload() without arguements"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.reload()

    def test_reload_with_args(self):
        """Test reload() with arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.reload(self, 2, 3, 4, 5)

    def class_reload_mismatch_test(self, cls_name):
        """Class test reload() mismatch for classname"""
        self.resetStorage()
        self.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        key = class_dict[cls_name]
        objs = key()
        storage.new(objs)
        k = f"{type(objs).__name__}.{objs.id}"
        storage.save()
        objs.name = "Trefa"
        storage.reload()
        self.assertEqual(objs.to_dict(), storage.all()[k].to_dict())

    def test_reload_mismatch_basemodel(self):
        """Tests reload_mismatch() method for BaseModel"""
        self.class_reload_mismatch_test("BaseModel")

    def test_reload_mismatch_user(self):
        """Tests reload_mismatch() method for User"""
        self.class_reload_mismatch_test("User")
        
    def test_reload_mismatch_place(self):
        """Tests reload_mismatch() method for Place"""
        self.class_reload_mismatch_test("Place")

    def test_reload_mismatch_city(self):
        """Tests reload_mismatch() method for City"""
        self.class_reload_mismatch_test("City")

    def test_reload_mismatch_review(self):
        """Tests reload_mismatch() method for Review"""
        self.class_reload_mismatch_test("Review")
    
    def test_reload_mismatch_state(self):
        """Tests reload_mismatch() method for State"""
        self.class_reload_mismatch_test("State")
    

    def test_reload_mismatch_amenity(self):
        """Tests reload_mismatch() method for Amenity"""
        self.class_reload_mismatch_test("Amenity")

if __name__ == "__main__":
    unittest.main()
