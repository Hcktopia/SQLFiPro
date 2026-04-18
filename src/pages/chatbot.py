import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(page_title="Interactive Chatbot", page_icon="🤖")

# Initialize session state variables if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
if "personality" not in st.session_state:
    st.session_state.personality = "professional"
if "max_history" not in st.session_state:
    st.session_state.max_history = 10

# Title and introduction
st.title("🤖 Interactive Chatbot")
st.markdown("""
    Welcome to the Interactive Chatbot demo! This page demonstrates a basic chatbot interface
    with customizable features. Use the sidebar to adjust settings and experiment with
    different chatbot personalities.
""")

# Sidebar configuration
with st.sidebar:
    st.header("Chatbot Settings")
    
    # Personality selector
    st.session_state.personality = st.radio(
        "Choose Chatbot Personality",
        ["professional", "friendly", "creative"],
        help="This setting affects the chatbot's response style"
    )
    
    # Message history length slider
    st.session_state.max_history = st.slider(
        "Maximum Message History",
        min_value=5,
        max_value=50,
        value=10,
        help="Control how many messages to keep in the chat history"
    )
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.success("Chat history cleared!")

# Educational section about chatbots
with st.expander("📚 How Do Chatbots Work?"):
    st.markdown("""
        ### Basic Concepts of Chatbots
        
        Chatbots are computer programs designed to simulate conversation with human users.
        They typically work through these steps:
        
        1. **Input Processing**: Receive and parse user messages
        2. **Understanding**: Analyze the message content and intent
        3. **Response Generation**: Create appropriate responses based on the input
        4. **Learning**: Some chatbots can learn from conversations (not implemented in this demo)
        
        This demo implements a simple rule-based chatbot for educational purposes.
    """)

# Function to generate bot responses based on personality
def get_bot_response(message, personality):
    # Simple response generation based on personality
    greetings = ["hello", "hi", "hey", "greetings"]
    if any(greeting in message.lower() for greeting in greetings):
        responses = {
            "professional": "Hello! How may I assist you today?",
            "friendly": "Hey there! 👋 What's on your mind?",
            "creative": "Greetings, wonderful human! 🌟 Ready for an adventure?"
        }
        return responses[personality]
    
    # Default responses for other messages
    default_responses = {
        "professional": "I understand. Please tell me more about your request.",
        "friendly": "That's interesting! Let's chat more about it! 😊",
        "creative": "Wow, that sparks so many fascinating ideas! 🎨 Let's explore further!"
    }
    return default_responses[personality]

# Display chat history
st.subheader("Chat History")
for message in st.session_state.messages[-st.session_state.max_history:]:
    with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "🤖"):
        st.write(f"{message['content']}")
        st.caption(f"Sent at {message['timestamp']}")

# Chat input
user_message = st.chat_input("Type your message here...")
if user_message:
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": user_message,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Generate and add bot response
    bot_response = get_bot_response(user_message, st.session_state.personality)
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Rerun to update the chat display
    st.rerun() 