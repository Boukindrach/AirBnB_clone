#!/usr/bin/python3

import unittest
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):
    def test_init(self):
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)

    def test_str(self):
        city = City()
        string_representation = str(city)
        self.assertIsInstance(string_representation, str)

if __name__ == '__main__':
    unittest.main()
