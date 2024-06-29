#!/usr/bin/python3
"""Test """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from sqlalchemy import Column, inspect
import unittest


class test_review(test_basemodel):
    """Test """

    def setUp(self):
        """
        Set up a test review instance.
        """
        self.review = Review()

    def test_table_name(self):
        """
        Test that the table name is correct.
        """
        self.assertEqual(Review.__tablename__, "reviews")

    def test_text_column(self):
        """
        Test the text column is defined correctly.
        """
        mapper = inspect(Review)
        text_column = mapper.columns.get('text')
        self.assertIsInstance(text_column, Column)
        self.assertEqual(text_column.type.length, 1024)
        self.assertFalse(text_column.nullable)

    def test_place_id_column(self):
        """
        Test the place_id column is defined correctly.
        """
        mapper = inspect(Review)
        place_id_column = mapper.columns.get('place_id')
        self.assertIsInstance(place_id_column, Column)
        self.assertEqual(place_id_column.type.length, 60)
        self.assertFalse(place_id_column.nullable)
        self.assertEqual(place_id_column.foreign_keys.pop().column.table.name, 'places')

    def test_user_id_column(self):
        """
        Test the user_id column is defined correctly.
        """
        mapper = inspect(Review)
        user_id_column = mapper.columns.get('user_id')
        self.assertIsInstance(user_id_column, Column)
        self.assertEqual(user_id_column.type.length, 60)
        self.assertFalse(user_id_column.nullable)
        self.assertEqual(user_id_column.foreign_keys.pop().column.table.name, 'users')


    @unittest.skipIf(True, "Relationships")
    def test_relationships(self):
        """
        Test the relationships are defined correctly.
        """
        mapper = inspect(Review)
        relationships = mapper.relationships

        # Check relationship with Place
        self.assertIn('place', relationships)
        place_relationship = relationships['place']
        self.assertEqual(place_relationship.argument, "Place")
        self.assertEqual(place_relationship.back_populates, 'reviews')

        # Check relationship with User
        self.assertIn('user', relationships)
        user_relationship = relationships['user']
        self.assertEqual(user_relationship.argument, "User")
        self.assertEqual(user_relationship.back_populates, 'reviews')
