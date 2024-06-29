#!/usr/bin/python3
"""Test """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from sqlalchemy import Column, inspect


class test_User(test_basemodel):
    """Test """

    def __init__(self, *args, **kwargs):
        """Test """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email_column(self):
        """
        Test the email column is defined correctly.
        """
        mapper = inspect(User)
        email_column = mapper.columns.get('email')
        self.assertIsInstance(email_column, Column)
        self.assertEqual(email_column.type.length, 128)
        self.assertFalse(email_column.nullable)

    def test_password_column(self):
        """
        Test the password column is defined correctly.
        """
        mapper = inspect(User)
        password_column = mapper.columns.get('password')
        self.assertIsInstance(password_column, Column)
        self.assertEqual(password_column.type.length, 128)
        self.assertFalse(password_column.nullable)

    def test_first_name_column(self):
        """
        Test the first_name column is defined correctly.
        """
        mapper = inspect(User)
        first_name_column = mapper.columns.get('first_name')
        self.assertIsInstance(first_name_column, Column)
        self.assertEqual(first_name_column.type.length, 128)

    def test_last_name_column(self):
        """
        Test the last_name column is defined correctly.
        """
        mapper = inspect(User)
        last_name_column = mapper.columns.get('last_name')
        self.assertIsInstance(last_name_column, Column)
        self.assertEqual(last_name_column.type.length, 128)

    def test_places_relationship(self):
        """
        Test the places relationship is defined correctly.
        """
        self.assertIn('places', User.__mapper__.relationships.keys())
        places_relationship = User.__mapper__.relationships['places']
        self.assertEqual(places_relationship.argument, "Place")
        self.assertEqual(places_relationship.backref, 'user')

    def test_reviews_relationship(self):
        """
        Test the reviews relationship is defined correctly.
        """
        self.assertIn('reviews', User.__mapper__.relationships.keys())
        reviews_relationship = User.__mapper__.relationships['reviews']
        self.assertEqual(reviews_relationship.argument, "Review")
        self.assertEqual(reviews_relationship.backref, 'user')
    
