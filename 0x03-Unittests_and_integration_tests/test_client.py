#!/usr/bin/env python3
"""
    Test Module for client
"""
from fixtures import TEST_PAYLOAD
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
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
        """ test if _public_repos_url returns correct result"""
        client = GithubOrgClient('url')
        with patch(
            'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_got:
            mock_got.return_value = {'repos_url': 'expected_url'}
            self.assertEqual(client._public_repos_url, 'expected_url')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ test if public_repos returns correct result"""
        client = GithubOrgClient('url')
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock_public_repo_url:
            # set return value of _public_repos_url property
            returned_repor_url = 'google.com'
            mock_public_repo_url.return_value = returned_repor_url
            mock_get_json.return_value = [{'name': 'googleDocs'}, {
                'name': 'googleSlides'}, {'name': 'googleSheets'}]
            expected_result = ['googleDocs', 'googleSlides', 'googleSheets']
            self.assertEqual(client.public_repos(), expected_result)
            mock_get_json.assert_called_once_with(returned_repor_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, result):
        """ test if has_license works correctly """
        # (repo: Dict[str, Dict], license_key: str) -> bool:
        self.assertEqual(GithubOrgClient.has_license(repo, license), result)


@parameterized_class((
    'org_payload',
    'repos_payload',
    'expected_repos',
    'apache2_rep'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(TestCase):
    """ test class to test integration of GithubOrgClient"""
    @classmethod
    def setUpClass(cls):
        """ Set up test method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ tear down test method"""
        cls.get_patcher.stop()

    def setUp(self):
        """Set up mock response for each test"""
        # Mock response with repos_payload
        mock_response_first = MagicMock()
        mock_response_first.json.return_value = self.org_payload

        mock_response_second = MagicMock()
        mock_response_second.json.return_value = self.repos_payload
        self.mock_get.side_effect = [mock_response_first, mock_response_second]
        # self.mock_get.return_value = self.repos_payload

    def test_public_repos(self):
        """ test public_repos with license is None"""
        client = GithubOrgClient(self.org_payload)
        self.assertEqual(client.public_repos(),
                         self.expected_repos)

    def test_public_repos_with_license(self):
        """ test public_repos with license is apache-2.0"""
        client = GithubOrgClient(self.org_payload)
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_rep)
