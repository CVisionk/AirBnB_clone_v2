#!/usr/bin/python3
"""Test """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from sqlalchemy import Column, String, inspect


class test_City(test_basemodel):
    """Test """

    def __init__(self, *args, **kwargs):
        """Test """
        super().__init__(*args, **kwargs)

    def test_name_column_attributes(self):
        """
        Test that the 'name' column of Amenity
        is a Column of type String with a maximum
        length of 128 and is not nullable.
        """
        mapper = inspect(City)
        name_column = mapper.columns.get('name')
        self.assertIsInstance(name_column, Column)
        self.assertIsInstance(name_column.type, String)
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

    def test_state_id(self):
        """
        Test state_id is Column of type string
        """
        mapper = inspect(City)
        state_id_c = mapper.columns.get('state_id')
        self.assertIsInstance(state_id_c, Column)
        self.assertIsInstance(state_id_c.type, String)
        self.assertEqual(state_id_c.type.length, 60)
        self.assertFalse(state_id_c.nullable)
        foreign_keys = state_id_c.foreign_keys
        self.assertTrue(any(fk for fk in foreign_keys if
                            fk.target_fullname == 'states.id'))
