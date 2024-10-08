// frontend/src/services/api.js

const API_URL = "http://localhost:5001";  // Backend API URL
// const API_URL = "https://studoraibackend-f0cdbf9798a6.herokuapp.com/";  // Backend API URL


// Function to send a chat message to the backend
export const sendMessage = async (message) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.error || "Something went wrong");
    }

    return data.response;  // Return the AI's response
  } catch (error) {
    console.error("Error communicating with the backend:", error);
    return null;  // Return null in case of an error
  }
};
