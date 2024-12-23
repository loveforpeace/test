// Function to map request data to the frontend fields
function mapRequestData() {
    return {
        data: {
            slices: [
                {
                    origin: document.getElementById('origin').value,
                    destination: document.getElementById('destination').value,
                    departure_time: {
                        from: document.getElementById('departure_time_from').value,
                        to: document.getElementById('departure_time_to').value
                    },
                    departure_date: document.getElementById('departure_date').value,
                    arrival_time: {
                        from: document.getElementById('arrival_time_from').value,
                        to: document.getElementById('arrival_time_to').value
                    }
                }
            ],
            private_fares: {
                QF: [
                    {
                        corporate_code: document.getElementById('qf_corporate_code').value,
                        tracking_reference: document.getElementById('qf_tracking_reference').value
                    }
                ],
                UA: [
                    {
                        corporate_code: document.getElementById('ua_corporate_code').value,
                        tour_code: document.getElementById('ua_tour_code').value
                    }
                ]
            },
            passengers: [
                {
                    family_name: document.getElementById('family_name').value,
                    given_name: document.getElementById('given_name').value,
                    loyalty_programme_accounts: [
                        {
                            account_number: document.getElementById('loyalty_account_number').value,
                            airline_iata_code: document.getElementById('loyalty_airline_iata_code').value
                        }
                    ],
                    type: document.getElementById('passenger_type').value
                },
                {
                    age: parseInt(document.getElementById('age').value, 10),
                    fare_type: document.getElementById('fare_type').value
                }
            ],
            max_connections: parseInt(document.getElementById('max_connections').value, 10),
            cabin_class: document.getElementById('cabin_class').value
        }
    };
}

// Function to handle the response data and map it to the frontend fields
function handleResponseData(responseData) {
    const offers = responseData.data.offers;
    offers.forEach(offer => {
        // Example of mapping response data to frontend fields
        document.getElementById('total_emissions_kg').innerText = offer.total_emissions_kg;
        document.getElementById('total_amount').innerText = offer.total_amount;
        // Add more mappings as needed
    });
}

// Function to send request to the backend
function fetchDuffelFlightsListOffers() {
    const requestData = mapRequestData();
    fetch('http://localhost:5000/duffel-flights-list-offers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'DUFFEL_API_KEY': 'your_api_key_here' // Replace with actual API key
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => handleResponseData(data))
    .catch(error => console.error('Error:', error));
}

// Event listener for form submission or button click
document.getElementById('fetch_offers_button').addEventListener('click', fetchDuffelFlightsListOffers);

// End of response