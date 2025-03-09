import os
from flask import Flask, request, Response, stream_with_context, jsonify
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Configuration
TARGET_API_BASE_URL = "https://api.scaleway.ai/f611bb39-9278-4dfb-8192-8e851cfc9dc6/v1"
API_KEY = os.getenv('SCW_API_KEY', 'c7bc12c1-00da-400e-bb5c-0027afac2602')

if not API_KEY:
    raise ValueError("SCW_API_KEY environment variable not set")

# Function to generate headers for the proxied request
def generate_headers():
    headers = {key: value for key, value in request.headers if key.lower() != 'host'}
    headers['Authorization'] = f"Bearer {API_KEY}"
    return headers

# Function to stream the response from the target API
def generate_streamed_response(resp):
    try:
        for chunk in resp.iter_content(chunk_size=4096):
            if chunk:
                yield chunk
    except GeneratorExit:
        resp.close()

# Add CORS headers to allow everything
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    response.headers['Access-Control-Allow-Credentials'] = 'true'  # Allow credentials
    response.headers['Access-Control-Allow-Headers'] = '*'  # Allow all headers
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'  # Explicitly allow HTTP methods
    return response

# Proxy route to handle all paths and methods
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def proxy(path):
    # Construct the target URL
    target_url = f"{TARGET_API_BASE_URL.rstrip('/')}/{path}" if path else TARGET_API_BASE_URL.rstrip('/')
    
    # Forward query parameters
    params = request.args.to_dict()

    # Get the appropriate headers
    headers = generate_headers()

    # Log the incoming request details
    app.logger.debug("\n" + "=" * 50)
    app.logger.debug("Incoming Request Details:")
    app.logger.debug(f"Method: {request.method}")
    app.logger.debug(f"Path: {path}")
    app.logger.debug(f"Headers: {dict(request.headers)}")
    app.logger.debug(f"Query Params: {params}")
    app.logger.debug(f"Body: {request.get_data().decode('utf-8', errors='replace')}")

    try:
        # Make the request to the target API with streaming enabled
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=params,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            stream=True,  # Enable streaming
        )

        # Log the upstream API response details
        app.logger.debug("\n" + "-" * 50)
        app.logger.debug("Upstream API Response Details:")
        app.logger.debug(f"URL: {resp.url}")
        app.logger.debug(f"Status Code: {resp.status_code}")
        app.logger.debug(f"Headers: {dict(resp.headers)}")
        app.logger.debug("-" * 50)

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error forwarding the request: {e}")
        return add_cors_headers(Response(f"Error forwarding the request: {e}", status=502))

    # Prepare the response headers
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    response_headers = [
        (name, value) for name, value in resp.headers.items()
        if name.lower() not in excluded_headers
    ]

    # Return a streamed response to the client
    return add_cors_headers(Response(
        stream_with_context(generate_streamed_response(resp)),
        status=resp.status_code,
        headers=response_headers
    ))

# Handle preflight (OPTIONS) requests
@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def options_handler(path):
    response = jsonify({'status': 'ok'})
    return add_cors_headers(response)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, threaded=True)
