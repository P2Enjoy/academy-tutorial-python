from flask import Flask, request, make_response
import requests
from pyngrok import ngrok
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("config.env")

app = Flask(__name__)

# Target base URL for proxying (backend you're proxying to)
PROXY_BASE_URL = "http://127.0.0.1:2024"  # Replace with your backend URL

# Add CORS headers to allow everything
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    response.headers['Access-Control-Allow-Credentials'] = 'true'  # Allow credentials
    response.headers['Access-Control-Allow-Headers'] = '*'  # Allow all headers
    response.headers['Access-Control-Allow-Methods'] = '*'  # Allow all HTTP methods
    return response

# Handle all routes and proxy requests
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def proxy(path):
    # Handle preflight OPTIONS requests
    if request.method == 'OPTIONS':
        return add_cors_headers(make_response())

    # Build the proxied request to the target server
    target_url = f"{PROXY_BASE_URL}/{path}"
    try:
        response = requests.request(
            method=request.method,
            url=target_url,
            headers={key: value for key, value in request.headers.items() if key.lower() != 'host'},
            params=request.args,
            data=request.get_data(),
            cookies=request.cookies,
        )

        # Build the response with proxied content and status
        flask_response = make_response(response.content, response.status_code)
        for key, value in response.headers.items():
            flask_response.headers[key] = value

        # Add CORS headers
        return add_cors_headers(flask_response)
    except requests.RequestException as e:
        return make_response(f"Error proxying request: {e}", 502)

# Handle favicon requests to avoid unnecessary errors
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with "No Content" status

if __name__ == '__main__':
    # Retrieve the ngrok authtoken from the .env file
    ngrok_authtoken = os.getenv("NGROK_AUTHTOKEN")

    # Authenticate ngrok with your authtoken
    ngrok.set_auth_token(ngrok_authtoken)

    # Start ngrok tunnel
    public_url = ngrok.connect(8123)
    print(f"ngrok tunnel: {public_url}")

    # Start Flask app
    app.run(host="0.0.0.0", port=8123)
