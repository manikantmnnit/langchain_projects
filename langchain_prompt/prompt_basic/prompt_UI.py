from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Analysis of python library")

topic_input=st.selectbox('Select library ',['Seaborn','sklearn','pathlib'])

style_input=st.selectbox('Select Explanation Style',["Basic Introduction","Explain with real example","Explain with code",'Explain with Math logic'])

length_input=st.selectbox('Select explanation length',['2-3 sentences', '2-3 paragraphs','long explanation'])

# Template
template=PromptTemplate(
    template="""Act as a research assistant and provide an explanation of the {topic_input} library. Ensure the explanation follows these guidelines:

Explanation Style: {style_input}

If 'Basic Introduction', provide a clear and concise overview of the library.

If 'Explain with real example', include a practical example or use case.

If 'Explain with code', provide a code snippet with comments to demonstrate its usage.

If 'Explain with Math logic', include mathematical formulations or logic behind the library's functionality.

Explanation Length: {length_input}

If '2-3 sentences', keep the explanation brief and to the point.

If '2-3 paragraphs', provide a moderately detailed explanation.

If 'long explanation', include a comprehensive breakdown with examples, code, or math as needed.

Additional Details:

Highlight the key features or functionalities of the {topic_input} library.

If applicable, explain how it compares to similar libraries or tools.

Use simple and clear language to ensure the explanation is accessible to beginners.""",
input_variables=['topic_input','length_input','style_input']
)

# fill the placeholder
prompt=template.invoke({
    'topic_input':topic_input,
    'length_input':length_input,
    'style_input':style_input
})



llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.5
)

if st.button('press to get answer'):
    result = llm.invoke(prompt)  # Invoking the model
    st.write(result.content if hasattr(result, 'content') else str(result))  # Ensure content extraction
