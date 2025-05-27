import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Placeholder for OpenAI API key (will be used later)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "AI-Powered Virtual Assistant Backend is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # This is a placeholder for the OpenAI API call
    # In the next step, we'll integrate the actual OpenAI call here.
    ai_response = f"You said: '{user_message}'. (AI response coming soon!)"

    return jsonify({"response": ai_response})

if __name__ == '__main__':
    # You can change the port if needed, e.g., port=5001
    app.run(debug=True, port=5000)