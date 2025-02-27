from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Paper Queries Tool")

user_input = st.text_input("Enter your prompt")

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0
)

if st.button('Summarize') and user_input:
    result = llm.invoke(user_input)  # Invoking the model
    st.write(result.content if hasattr(result, 'content') else str(result))  # Ensure content extraction
