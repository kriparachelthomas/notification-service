from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Notification Service!"})

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    
    # Simulate sending a notification (e.g., via email or SMS)
    print(f"Sending notification to user {user_id}: {message}")

    return jsonify({"status": "Notification sent", "user_id": user_id, "message": message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
