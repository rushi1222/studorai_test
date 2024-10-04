import os
from quart import Quart, request, jsonify
from quart_cors import cors
from openai import AsyncOpenAI
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Setup Quart app with CORS
app = Quart(__name__)
app = cors(app, allow_origin="*")

# Setup logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Async client for OpenAI
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()
    user_input = data.get("message")

    # Log the received message
    logging.info(f"Received message from client: {user_input}")

    try:
        # Log the API Key being used (ensure it's properly loaded)
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logging.error("OPENAI_API_KEY is not set!")
            return jsonify({"error": "OPENAI_API_KEY is missing"}), 500
        
        logging.info(f"Using API Key: {api_key}")

        # Log before sending request to OpenAI API
        logging.info("Sending request to OpenAI API")

        # Use the OpenAI async client to get a response
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )

        # Log the response from OpenAI
        logging.info(f"OpenAI Response: {response}")

        # Extract the AI's reply
        reply = response.choices[0].message.content.strip()

        # Send the response back to the frontend
        return jsonify({"response": reply})

    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error while communicating with OpenAI API: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Entry point for running the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
