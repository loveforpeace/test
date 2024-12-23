// Global variable to store the access token
let access_token = null;

// Function to request the OAuth token
async function requestOAuthToken() {
    const url = 'http://localhost:5000/amadeus-oauth';
    const requestBody = {
        grant_type: "client_credentials",
        client_id: "YOUR_API_KEY",
        client_secret: "YOUR_API_SECRET"
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const responseData = await response.json();
        console.log("Response Status Code:", response.status);
        console.log("Response Data:", responseData);

        if (response.status === 200) {
            access_token = responseData.access_token;
        }
    } catch (error) {
        console.error("Error fetching OAuth token:", error);
    }
}

// Call the function to request the OAuth token
requestOAuthToken();
// The following code is the backend Flask application that handles the OAuth token request.