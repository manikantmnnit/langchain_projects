from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

# load_dotenv()


st.header('General Knowledge tool')

llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

# Get user input
user_input = st.text_input("Enter your General Awareness Question:")

if st.button("Answer") and user_input:
    model=ChatHuggingFace(llm=llm)
    result = model.invoke(user_input)  # Call the model
    response_text = result.content() if isinstance(result, str) else str(result)  # Ensure we get text output
    st.write(response_text)


