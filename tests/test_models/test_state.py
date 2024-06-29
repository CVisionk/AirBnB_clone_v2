#!/usr/bin/python3
"""Test """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from os import getenv
from sqlalchemy import Column, String, inspect
import models


class test_state(test_basemodel):
    """Test """

    def setUp(self):
        """
        Set up a test state instance.
        """
        self.state = State()

    def test_table_name(self):
        """
        Test that the table name is correct.
        """
        self.assertEqual(State.__tablename__, "states")

    def test_name_column(self):
        """
        Test the name column is defined correctly.
        """
        mapper = inspect(State)
        name_column = mapper.columns.get('name')
        self.assertIsInstance(name_column, Column)
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

    def test_cities_relationship_db(self):
        """
        Test the cities relationship is defined correctly for database storage.
        """
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertIn('cities', State.__mapper__.relationships.keys())
            cities_relationship = State.__mapper__.relationships['cities']
            self.assertEqual(cities_relationship.argument, City)
            self.assertEqual(cities_relationship.backref[0], 'state')
            self.assertEqual(cities_relationship.cascade, 'all, delete-orphan')