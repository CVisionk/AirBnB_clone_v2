#!/usr/bin/python3
"""Test """
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import unittest
from sqlalchemy import Column, inspect, Integer, Float
import models



class test_Place(test_basemodel):
    """Test """

    def setUp(self):
        """
        Set up a test place instance.
        """
        self.place = Place()

    def test_table_name(self):
        """
        Test that the table name is correct.
        """
        self.assertEqual(Place.__tablename__, "places")

    def test_columns(self):
        """
        Test that all columns are correctly defined.
        """
        mapper = inspect(Place)

        # Test city_id column
        city_id_column = mapper.columns.get('city_id')
        self.assertIsInstance(city_id_column, Column)
        self.assertEqual(city_id_column.type.length, 60)
        self.assertFalse(city_id_column.nullable)
        self.assertEqual(city_id_column.foreign_keys.pop().column.table.name, 'cities')

        # Test user_id column
        user_id_column = mapper.columns.get('user_id')
        self.assertIsInstance(user_id_column, Column)
        self.assertEqual(user_id_column.type.length, 60)
        self.assertFalse(user_id_column.nullable)
        self.assertEqual(user_id_column.foreign_keys.pop().column.table.name, 'users')

        # Test name column
        name_column = mapper.columns.get('name')
        self.assertIsInstance(name_column, Column)
        self.assertEqual(name_column.type.length, 128)
        self.assertFalse(name_column.nullable)

        # Test description column
        description_column = mapper.columns.get('description')
        self.assertIsInstance(description_column, Column)
        self.assertEqual(description_column.type.length, 1024)

        # Test number_rooms column
        number_rooms_column = mapper.columns.get('number_rooms')
        self.assertIsInstance(number_rooms_column, Column)
        #self.assertEqual(number_rooms_column.type, Integer)
        #self.assertEqual(number_rooms_column.default, 0)

        # Test number_bathrooms column
        number_bathrooms_column = mapper.columns.get('number_bathrooms')
        self.assertIsInstance(number_bathrooms_column, Column)
        #self.assertEqual(number_bathrooms_column.type, Integer)
        #self.assertEqual(number_bathrooms_column.default, 0)

        # Test max_guest column
        max_guest_column = mapper.columns.get('max_guest')
        self.assertIsInstance(max_guest_column, Column)
        #self.assertEqual(max_guest_column.type, Integer)
        #self.assertEqual(max_guest_column.default, 0)

        # Test price_by_night column
        price_by_night_column = mapper.columns.get('price_by_night')
        self.assertIsInstance(price_by_night_column, Column)
        #self.assertEqual(price_by_night_column.type, Integer)
        #self.assertEqual(price_by_night_column.default, 0)

        # Test latitude column
        latitude_column = mapper.columns.get('latitude')
        self.assertIsInstance(latitude_column, Column)
        #self.assertEqual(latitude_column.type, Float)

        # Test longitude column
        longitude_column = mapper.columns.get('longitude')
        self.assertIsInstance(longitude_column, Column)
        #self.assertEqual(longitude_column.type, Float)

    @unittest.skipIf(True, "relationship")
    def test_relationships(self):
        """
        Test that the relationships are defined correctly.
        """
        mapper = inspect(Place)
        relationships = mapper.relationships

        # Test reviews relationship
        self.assertIn('reviews', relationships)
        reviews_relationship = relationships['reviews']
        self.assertEqual(reviews_relationship.argument, Review)
        self.assertEqual(reviews_relationship.backref[0], 'place')
        self.assertEqual(reviews_relationship.cascade, 'delete')

        # Test amenities relationship
        self.assertIn('amenities', relationships)
        amenities_relationship = relationships['amenities']
        self.assertEqual(amenities_relationship.argument, Amenity)
        self.assertEqual(amenities_relationship.secondary.name, 'place_amenity')

    @unittest.skipIf(True, "Storage")
    def test_reviews_property_file(self):
        """
        Test the reviews property for file storage.
        """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            place = Place(id='place_id')
            review1 = Review(id='review1_id', place_id='place_id')
            review2 = Review(id='review2_id', place_id='place_id')
            review3 = Review(id='review3_id', place_id='other_place_id')

            models.storage.new(place)
            models.storage.new(review1)
            models.storage.new(review2)
            models.storage.new(review3)
            models.storage.save()

            self.assertEqual(len(place.reviews), 2)
            self.assertIn(review1, place.reviews)
            self.assertIn(review2, place.reviews)
            self.assertNotIn(review3, place.reviews)

    @unittest.skipIf(True, "Storage test")
    def test_amenities_property_file(self):
        """
        Test the amenities property for file storage.
        """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            place = Place(id='place_id', amenity_ids=['amenity1_id', 'amenity2_id'])
            amenity1 = Amenity(id='amenity1_id')
            amenity2 = Amenity(id='amenity2_id')
            amenity3 = Amenity(id='amenity3_id')

            models.storage.new(place)
            models.storage.new(amenity1)
            models.storage.new(amenity2)
            models.storage.new(amenity3)
            models.storage.save()

            self.assertEqual(len(place.amenities), 2)
            self.assertIn(amenity1, place.amenities)
            self.assertIn(amenity2, place.amenities)
            self.assertNotIn(amenity3, place.amenities)

            # Test adding an amenity via setter
            place.amenities = [amenity3]
            self.assertIn(amenity3, place.amenities)
            self.assertEqual(len(place.amenities), 1)

