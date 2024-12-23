from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Allow CORS if not already set
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# New route for Duffel flights list offers
@app.route('/duffel-flights-list-offers', methods=['POST'])
def duffel_flights_list_offers():
    url = 'https://api.duffel.com/air/offer_requests'
    headers = {
        "Accept-Encoding": "gzip",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Duffel-Version": "v2",
        "Authorization": f"Bearer {request.headers.get('DUFFEL_API_KEY')}"
    }
    data = request.json
    response = requests.post(url, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)