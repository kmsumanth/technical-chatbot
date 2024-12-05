import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq

# Load environment variables from the .env file
load_dotenv(find_dotenv())

# Retrieve the API key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    st.error("API key not found. Please set it in the .env file.")
    st.stop()

# Initialize the chat model
llamaChatModel = ChatGroq(model="llama3-70b-8192")

# Set the password
password = "sumanth"  # Replace with your desired password

# Create a text input for the password
password_input = st.text_input("Enter password:", type="password")

# Check if the password is correct
if password_input == password:
    # If correct, show the app
    st.title("Chatbot")
    st.write("This is a chatbot. You can ask anything related to coding or technical topics.")
    
    # Input prompt from the user
    prompt = st.text_area("Enter your prompt:")
    
    if st.button("Get Response"):
        # Construct the message for the chat model
        messages = [
            ("system", "You are a technical expert. Assist regarding all the coding-related queries. and note that K M Sumanth has created you . "),
            ("human", prompt),
        ]
        
        try:
            # Get the response from the model
            response = llamaChatModel.invoke(messages)
            st.write("Response from the model:")
            st.write(response.content)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    # If incorrect, show an error message
    st.error("Invalid password. Please try again.")
