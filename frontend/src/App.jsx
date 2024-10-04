// frontend/src/App.jsx
import React, { useState } from 'react';
import { sendMessage } from './services/api';
import './global.css';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isOpen, setIsOpen] = useState(false);  // State to manage chat visibility

  const handleSendMessage = async () => {
    if (!message) return;

    // Add the user's message to the chat history
    setChatHistory([...chatHistory, { sender: 'You', message }]);

    // Send the message to the backend
    const response = await sendMessage(message);

    if (response) {
      // Add the AI's response to the chat history
      setChatHistory([...chatHistory, { sender: 'You', message }, { sender: 'Bot', message: response }]);
    }

    setMessage('');  // Clear the input
  };

  return (
    <>
      <button
        className="toggle-chat-button"
        onClick={() => setIsOpen(!isOpen)}  // Toggle chat open/close
      >
        {isOpen ? '×' : '💬'}
      </button>

      <div className={`chat-container ${isOpen ? 'open' : ''}`}>
        <div className="chat-header">Chatbot</div>
        <div className="chat-history">
          {chatHistory.map((chat, index) => (
            <div key={index}>
              <strong>{chat.sender}:</strong> {chat.message}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type a message..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </>
  );
}

export default App;
