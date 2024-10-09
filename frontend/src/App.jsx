import React, { useState } from 'react';
import { sendMessage } from './services/api';
import './global.css';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isOpen, setIsOpen] = useState(false);  // State to manage chat visibility
  const [loading, setLoading] = useState(false);  // Typing indicator state

  const handleSendMessage = async () => {
    if (!message) return;

    // Add the user's message to the chat history
    setChatHistory((prev) => [...prev, { sender: 'You', message }]);
    setLoading(true);  // Show typing indicator

    // Send the message to the backend
    const response = await sendMessage(message);

    if (response) {
      // Add the bot's response to the chat history separately
      setChatHistory((prev) => [...prev, { sender: 'Bot', message: response }]);
    }

    setMessage('');  // Clear the input
    setLoading(false);  // Hide typing indicator
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
            <div
              key={index}
              className={`chat-message ${chat.sender === 'You' ? 'user-message' : 'bot-message'}`}
            >
              {chat.message}
            </div>
          ))}
          {loading && (
            <div className="typing-indicator">
              <div className="dot"></div>
              <div className="dot"></div>
              <div className="dot"></div>
            </div>
          )}
        </div>
        <div className="chat-input-container">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type a message..."
            className="chat-input"
          />
          <button className="send-icon" onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </>
  );
}

export default App;
