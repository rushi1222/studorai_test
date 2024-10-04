import os
from quart import Quart, request, jsonify
from quart_cors import cors  # To handle CORS for React
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Quart(__name__)
app = cors(app, allow_origin="*")  # Allow CORS so React can interact with the API

# Instantiate the Async client
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Simple root route to avoid 404 errors
@app.route('/')
async def index():
    return "Backend is running!"

# API route to handle AI chat requests
@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()  # Get JSON data from React
    user_input = data.get("message")

    try:
        # Use the OpenAI async client to get a response
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})  # Send the reply back to React

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
