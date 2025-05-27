import axios from 'axios';
import { useState } from 'react';
import './App.css'; // We will create this file

function App() {
  const [messages, setMessages] = useState([]); // Stores chat history
  const [inputMessage, setInputMessage] = useState(''); // Stores current message in input field
  const [isLoading, setIsLoading] = useState(false); // To show loading indicator

  const BACKEND_URL = 'http://127.0.0.1:5000'; // Your Flask backend URL

  const sendMessage = async () => {
    if (inputMessage.trim() === '') return; // Don't send empty messages

    const userMessage = { text: inputMessage, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]); // Add user message to history
    setInputMessage(''); // Clear input field
    setIsLoading(true); // Start loading

    try {
      const response = await axios.post(`${BACKEND_URL}/chat`, {
        message: inputMessage,
      });

      const aiMessage = { text: response.data.response, sender: 'ai' };
      setMessages((prevMessages) => [...prevMessages, aiMessage]); // Add AI message to history
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { text: 'Oops! Something went wrong. Please try again.', sender: 'ai' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false); // Stop loading
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !isLoading) {
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <h1>AI Virtual Assistant</h1>
      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`message-bubble ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && <div className="message-bubble ai loading">AI is typing...</div>}
      </div>
      <div className="input-box">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
          disabled={isLoading}
        />
        <button onClick={sendMessage} disabled={isLoading}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;