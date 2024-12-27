from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for authentication
FINNHUB_SECRET = "ctn7a89r01qjlgirjmfg"

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Check if the Content-Type is application/json
    if request.content_type != 'application/json':
        return jsonify({"error": "Invalid Content-Type. Expected application/json"}), 415

    # Verify the source of the request
    if request.headers.get('X-Finnhub-Secret') != FINNHUB_SECRET:
        return jsonify({"error": "Unauthorized"}), 401

    # Acknowledge receipt quickly
    data = request.json
    print("Received data:", data)  # Log incoming data for debugging

    # Return a 2xx response to keep the webhook active
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
