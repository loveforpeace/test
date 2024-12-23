import unittest
import requests
from flask import Flask
from app import app

class DuffelFlightsListOffersIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.url = '/duffel-flights-list-offers'
        self.headers = {
            "Content-Type": "application/json",
            "DUFFEL_API_KEY": "your_test_api_key"  # Replace with a valid test API key
        }
        self.valid_payload = {
            # Add a valid payload structure here
        }

    def test_duffel_flights_list_offers_success(self):
        response = self.app.post(self.url, headers=self.headers, json=self.valid_payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_duffel_flights_list_offers_missing_api_key(self):
        headers = self.headers.copy()
        headers.pop("DUFFEL_API_KEY")
        response = self.app.post(self.url, headers=headers, json=self.valid_payload)
        self.assertEqual(response.status_code, 401)  # Assuming 401 for missing API key

    def test_duffel_flights_list_offers_invalid_payload(self):
        invalid_payload = {
            # Add an invalid payload structure here
        }
        response = self.app.post(self.url, headers=self.headers, json=invalid_payload)
        self.assertEqual(response.status_code, 400)  # Assuming 400 for bad request

if __name__ == '__main__':
    unittest.main()