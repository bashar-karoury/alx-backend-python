#!/usr/bin/env python3
"""
    Test Module for utils
"""
from unittest.mock import patch
from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """ Test Class for access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, seq, expected):
        """ test if access_nested_map returns correct result"""
        self.assertEqual(access_nested_map(map, seq), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, seq):
        """ test if access_nested_map returns correct result"""
        with self.assertRaises(KeyError):
            access_nested_map(map, seq)


class TestGetJson(TestCase):
    """ Test Class for get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_json):
        """ test if get_json returns correct result"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_json
            self.assertEqual(get_json(url), expected_json)
            mock_get.assert_called_once_with(url)
