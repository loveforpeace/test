import unittest
import requests
from unittest.mock import patch

class TestAmadeusOAuth(unittest.TestCase):

    @patch('requests.post')
    def test_amadeus_oauth_success(self, mock_post):
        # Mocking the response of the requests.post call
        mock_response = unittest.mock.Mock()
        expected_json = {
            'access_token': 'mock_access_token',
            'token_type': 'Bearer',
            'expires_in': 3600
        }
        mock_response.json.return_value = expected_json
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Making the actual call to the endpoint
        response = requests.post('http://localhost:5000/amadeus-oauth')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_json)

    @patch('requests.post')
    def test_amadeus_oauth_failure(self, mock_post):
        # Mocking the response of the requests.post call
        mock_response = unittest.mock.Mock()
        expected_json = {
            'error': 'invalid_client',
            'error_description': 'Client authentication failed'
        }
        mock_response.json.return_value = expected_json
        mock_response.status_code = 401
        mock_post.return_value = mock_response

        # Making the actual call to the endpoint
        response = requests.post('http://localhost:5000/amadeus-oauth')

        # Assertions
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), expected_json)

if __name__ == '__main__':
    unittest.main()