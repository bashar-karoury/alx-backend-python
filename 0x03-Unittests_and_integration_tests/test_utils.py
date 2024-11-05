#!/usr/bin/env python3
"""
    Test Module for utils
"""
from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map


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
