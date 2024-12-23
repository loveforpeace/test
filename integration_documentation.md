# Amadeus API Integration Documentation

## General Overview

This documentation provides a comprehensive guide for integrating with the Amadeus API using a Flask backend and a frontend component. The integration allows you to authenticate with the Amadeus API using OAuth2 and access various travel-related services provided by Amadeus. The backend handles the OAuth2 authentication process and stores the access token for subsequent API requests.

## Quick Start Guide

### Prerequisites

- Python 3.x
- Flask
- Flask-CORS
- Requests library
- Node.js and npm (for frontend)
- Amadeus API credentials (client ID and client secret)

### Backend Setup

#### Running Locally

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Ensure you have Python and pip installed. Then, install the required Python packages:

   ```bash
   pip install flask flask-cors requests
   ```

3. **Configure API Credentials:**

   Open `app.py` and replace `YOUR_API_KEY` and `YOUR_API_SECRET` with your Amadeus API credentials.

4. **Run the Backend Server:**

   Start the Flask server:

   ```bash
   python app.py
   ```

   The server will run on `http://localhost:5000`.

#### Running Remotely

1. **Deploy to a Cloud Provider:**

   You can deploy the Flask app to any cloud provider that supports Python applications, such as Heroku, AWS, or Google Cloud Platform.

2. **Environment Variables:**

   Set the `client_id` and `client_secret` as environment variables on your cloud platform.

3. **Start the Server:**

   Follow the cloud provider's instructions to start the server.

### Frontend Setup

#### Running Locally

1. **Navigate to Frontend Directory:**

   ```bash
   cd <frontend-directory>
   ```

2. **Install Dependencies:**

   Ensure you have Node.js and npm installed. Then, install the required packages:

   ```bash
   npm install
   ```

3. **Run the Frontend:**

   Start the frontend development server:

   ```bash
   npm start
   ```

   The frontend will typically run on `http://localhost:3000`.

#### Running Remotely

1. **Build the Frontend:**

   Create a production build of the frontend:

   ```bash
   npm run build
   ```

2. **Deploy to a Hosting Service:**

   Deploy the build directory to a static hosting service like Vercel, Netlify, or AWS S3.

### Testing Options

- **Integration Tests:**

  Integration tests are available in the `integration_tests.py` file. To run the tests, use:

  ```bash
  python integration_tests.py
  ```

  Ensure the backend server is running before executing the tests.

## Troubleshooting Guide

- **Common Issues:**

  - **Invalid Credentials:** Ensure that the `client_id` and `client_secret` are correctly set in `app.py`.
  - **CORS Errors:** Make sure Flask-CORS is properly configured to allow requests from your frontend domain.
  - **Network Issues:** Verify that your network allows outbound requests to `https://test.api.amadeus.com`.

- **Debugging Tips:**

  - Check the console output for request and response logs.
  - Use tools like Postman to manually test API endpoints.

## Support Contact Information

For support related to this integration, please contact:

- **Email:** support@example.com
- **Phone:** +1-800-555-0199

## Links to API Provider Docs

- [Amadeus API Documentation](https://developers.amadeus.com/self-service)
- [OAuth2 Authentication Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)

This documentation should help you set up and troubleshoot the Amadeus API integration effectively. For further assistance, refer to the support contact information provided above.