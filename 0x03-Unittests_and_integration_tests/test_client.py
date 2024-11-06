#!/usr/bin/env python3
"""
    Test Module for client
"""
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Test Class for org method"""
    @parameterized.expand([
        ('google', 'google'),
        ('abc', 'abc')
    ])
    @patch('client.get_json')
    def test_org(self, url, expected, mock_get_json):
        """ test if org returns correct result"""
        client = GithubOrgClient(url)
        mock_get_json.return_value = expected
        self.assertEqual(client.org, expected)
        called_with = client.ORG_URL.format(org=client._org_name)
        mock_get_json.assert_called_once_with(called_with)

    def test_public_repos_url(self):
        """ test if org returns correct result"""
        client = GithubOrgClient('url')
        with patch(
            'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_got:
            mock_got.return_value = {'repos_url': 'expected_url'}
            self.assertEqual(client._public_repos_url, 'expected_url')
