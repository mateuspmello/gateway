import json
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from polls.views import get_token

class GetTokenTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_token')

    @patch('polls.views.requests.post')
    def test_get_token_success(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'access_token': 'test_token'}

        headers = {
            'HTTP_GRANT_TYPE': 'password',
            'HTTP_CLIENT_ID': 'test_client_id',
            'HTTP_CLIENT_SECRET': 'test_client_secret',
            'HTTP_USERNAME': 'test_username',
            'HTTP_PASSWORD': 'test_password'
        }

        response = self.client.get(self.url, **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'test_token')

    @patch('polls.views.requests.post')
    def test_get_token_invalid_credentials(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 401
        mock_response.json.return_value = {'error': 'Invalid credentials'}

        headers = {
            'HTTP_GRANT_TYPE': 'password',
            'HTTP_CLIENT_ID': 'test_client_id',
            'HTTP_CLIENT_SECRET': 'test_client_secret',
            'HTTP_USERNAME': 'test_username',
            'HTTP_PASSWORD': 'test_password'
        }

        response = self.client.get(self.url, **headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid credentials'})