import os
from quart import Quart, request, jsonify
from quart_cors import cors
from openai import AsyncOpenAI
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

app = Quart(__name__)
app = cors(app, allow_origin="*")

# Setup logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Async client
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()
    user_input = data.get("message")

    # Log the received message
    logging.info(f"Received message: {user_input}")

    try:
        # Log API Key
        logging.info(f"Using API Key: {os.getenv('OPENAI_API_KEY')}")

        # Use the OpenAI async client to get a response
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )

        # Log the response
        logging.info(f"AI Response: {response}")

        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})

    except Exception as e:
        # Log the error in detail
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
