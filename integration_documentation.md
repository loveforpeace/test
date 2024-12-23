# Duffel Flights API Integration Documentation

## General Overview

This documentation provides a comprehensive guide to integrating with the Duffel Flights API using a Flask backend and a frontend component. The integration allows users to list flight offers by sending requests to Duffel's API. The backend is implemented in Python using Flask, and it handles requests to Duffel's API. The frontend component interacts with this backend to display flight offers to users.

## Quick Start Guide

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Node.js and npm (for frontend, if applicable)
- Duffel API Key

### Backend Setup

#### Running Locally

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Ensure you have Python and pip installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**

   Start the Flask server:

   ```bash
   python app.py
   ```

   The server will run on `http://localhost:5000`.

#### Running Remotely

1. **Deploy to a Cloud Provider**

   - Choose a cloud provider (e.g., AWS, Heroku, Google Cloud).
   - Follow the provider's instructions to deploy a Flask application.
   - Ensure the environment has Python and pip installed.
   - Set the `DUFFEL_API_KEY` as an environment variable on the server.

2. **Access the Server**

   - Once deployed, access the server using the provided URL by the cloud provider.

### Frontend Setup

#### Running Locally

1. **Navigate to Frontend Directory**

   ```bash
   cd <frontend-directory>
   ```

2. **Install Dependencies**

   Ensure you have Node.js and npm installed. Then, install the required packages:

   ```bash
   npm install
   ```

3. **Run the Frontend**

   Start the frontend application:

   ```bash
   npm start
   ```

   The application will run on `http://localhost:3000` (or another port if specified).

#### Running Remotely

1. **Deploy to a Cloud Provider**

   - Choose a cloud provider (e.g., Netlify, Vercel).
   - Follow the provider's instructions to deploy a frontend application.
   - Ensure the environment is set up with Node.js and npm.

2. **Access the Application**

   - Once deployed, access the application using the provided URL by the cloud provider.

### Testing Options

- **Integration Tests**

  Integration tests are available in the `integration_tests.py` file. To run the tests, execute:

  ```bash
  python integration_tests.py
  ```

  Ensure the backend server is running before executing the tests.

## Troubleshooting Guide

- **CORS Issues**

  If you encounter CORS issues, ensure that the backend server is correctly setting CORS headers. The provided code already includes CORS settings.

- **API Key Errors**

  Ensure that the `DUFFEL_API_KEY` is correctly set in the request headers. Verify that the key is valid and has the necessary permissions.

- **Network Errors**

  Check your network connection and ensure that the Duffel API endpoint is reachable.

## Support Contact Information

For support, please contact:

- **Email:** support@example.com
- **Phone:** +1-234-567-890

## Links to API Provider Documentation

- [Duffel API Documentation](https://duffel.com/docs/api)

This documentation provides detailed information on the available endpoints, request/response formats, and authentication methods.