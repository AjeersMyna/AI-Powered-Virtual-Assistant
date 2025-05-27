import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI # Import the OpenAI client

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Initialize OpenAI client with your API key
# The API key is loaded from .env automatically by os.getenv
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "AI-Powered Virtual Assistant Backend is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Define the system prompt for the chatbot's persona
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant. You answer questions concisely and politely."},
            {"role": "user", "content": user_message}
        ]

        # Make the OpenAI API call
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo", # You can try other models like "gpt-4" if you have access
            messages=messages,
            temperature=0.7, # Controls randomness: lower for more focused, higher for more creative
            max_tokens=150 # Limits the length of the response
        )

        # Extract the AI's response
        ai_response = chat_completion.choices[0].message.content
        # You might want to log the full response for debugging: print(chat_completion)

        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return jsonify({"error": "Failed to get response from AI. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)