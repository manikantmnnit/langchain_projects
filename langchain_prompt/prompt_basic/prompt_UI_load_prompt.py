#%%
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
from langchain_core.
import streamlit as st

load_dotenv()

st.header("Analysis of python library")

topic_input=st.selectbox('Select library ',['Seaborn','sklearn','pathlib'])

style_input=st.selectbox('Select Explanation Style',["Basic Introduction","Explain with real example","Explain with code",'Explain with Math logic'])

length_input=st.selectbox('Select explanation length',['2-3 sentences', '2-3 paragraphs','long explanation'])

template=load_prompt('template.json')


llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.5
)

if st.button('press to get answer'):
    chain=template|llm 
    result=chain.invoke({  # # Invoking the chain
    'topic_input':topic_input,
    'length_input':length_input,
    'style_input':style_input
})
    st.write(result.content if hasattr(result, 'content') else str(result))  # Ensure content extraction



# %%
