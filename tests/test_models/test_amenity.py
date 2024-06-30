#!/usr/bin/python3
"""
Test:
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy import Column, String, inspect


class test_Amenity(test_basemodel):
    """
    Test Amenity
    """

    def __init__(self, *args, **kwargs):
        """Test """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_column_attributes(self):
        """
        Test that the 'name' column of Amenity is
        a Column of type String with a maximum length
        of 128 and is not nullable.
        """
        mapper = inspect(Amenity)
        name_column = mapper.columns.get('name')
        self.assertIsInstance(name_column, Column)
        self.assertIsInstance(name_column.type, String)
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)
