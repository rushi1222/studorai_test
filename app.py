from quart import Quart, request, jsonify
from quart_cors import cors
import logging
from services.openai_client import get_openai_client
from services.prompt_engineering import construct_prompt  # Use the updated construct_prompt
from services.utils import load_user_data

# Setup Quart app with CORS
app = Quart(__name__)
app = cors(app, allow_origin="*")

# Setup logging
logging.basicConfig(level=logging.INFO)

# Instantiate the OpenAI client
client = get_openai_client()

# In-memory dictionary to track if Alejandra has been greeted
greeted_users = {}

@app.route('/')
async def home():
    return "API is running"

@app.route('/chat', methods=['POST'])
async def chat():
    data = await request.get_json()
    user_input = data.get("message", "").strip()  # Get the message or default to an empty string if no input
    user_id = "alejandra"  # You can replace this with a unique identifier for different users

    # Log the received message
    logging.info(f"Received message from client: {user_input}")

    try:
        # Load the user.txt content to provide context
        user_data = load_user_data()
        if not user_data:
            return jsonify({"error": "user.txt file is missing or empty"}), 500

        # Check if the user has already been greeted
        if user_id not in greeted_users:
            greeted_users[user_id] = False  # Initialize if not greeted yet

        # If the user hasn't been greeted yet, start with a greeting
        if not greeted_users[user_id]:
            # Construct the greeting prompt
            prompt = [
                {"role": "system", "content": "You are an AI assistant for Alejandra, a 17-year-old high school student"},
                {"role": "assistant", "content": "Hi Alejandra, how can I help you today? (Options: 'Career Interests', 'College Applications', 'Goals and Ambitions')"}
            ]
            greeted_users[user_id] = True  # Mark the user as greeted
        else:
            # Construct the prompt based on user input and user data for subsequent interactions
            prompt = construct_prompt(user_data, user_input)

        # Log the constructed prompt before sending to OpenAI API
        logging.info(f"Constructed prompt: {prompt}")

        # Use the OpenAI async client to get a response
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=prompt,
            max_tokens=300,  # Adjust if needed
            temperature=0.5  # Adjust as needed
        )

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
