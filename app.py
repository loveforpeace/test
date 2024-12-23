from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Allow CORS if not existing
from flask_cors import CORS
CORS(app)

# Global access token variable
access_token = None

@app.route('/amadeus-oauth', methods=['POST'])
def amadeus_oauth():
    global access_token
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": "YOUR_API_KEY",
        "client_secret": "YOUR_API_SECRET"
    }
    print("Request Data:", data)
    response = requests.post(url, headers=headers, data=data)
    print("Response Status Code:", response.status_code)
    print("Response Data:", response.json())
    if response.status_code == 200:
        access_token = response.json().get('access_token')
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)
// The JavaScript code in `src/main/resources/js/app.js` is designed to interact with the Flask backend defined in `app.py`. 
// It sends a POST request to the `/amadeus-oauth` endpoint to obtain an OAuth token and logs the response.