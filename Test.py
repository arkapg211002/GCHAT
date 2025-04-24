import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAHX6Zl-x5iNQQnGnWtjLxYJ6VTdkq0Zfo")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)

# Streamlit App UI
st.set_page_config(page_title="Chat with Gemini", page_icon="💬", layout="wide")
st.title("🤖 Chat with Gemini")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Gemini response
    response = gemini_model.generate_content(user_input)
    ai_response = response.text

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    st.session_state.messages.append({"role": "assistant", "content": ai_response})
