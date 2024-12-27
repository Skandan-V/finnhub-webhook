from flask import Flask, request, jsonify

app = Flask(__name__)

# Update Secret key for authentication
FINNHUB_SECRET = "ctn82r9r01qjlgirl9i0ctn82r9r01qjlgirl9ig"

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Log headers and body for troubleshooting
    print("Headers:", request.headers)
    print("Request Body:", request.get_data())

    # Check if the Content-Type is application/json
    if request.content_type != 'application/json':
        print(f"Invalid Content-Type: {request.content_type}")  # Log invalid Content-Type
        return jsonify({"error": "Invalid Content-Type. Expected application/json"}), 415

    # Verify the source of the request
    if request.headers.get('X-Finnhub-Secret') != FINNHUB_SECRET:
        return jsonify({"error": "Unauthorized"}), 401

    # Process the incoming data
    try:
        data = request.json
        print("Received data:", data)  # Log incoming data for debugging
    except Exception as e:
        print(f"Error parsing JSON: {str(e)}")  # Log JSON parsing error
        return jsonify({"error": "Failed to parse JSON"}), 400

    # Acknowledge the receipt of the event
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
