from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm= ChatOpenAI()

prompt1=PromptTemplate(
    template="Provide the detailed description about {topic} in python library",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Provide me short summary about following text \n {detailed_text}",
    input_variables=['detailed_text']
)

parser=StrOutputParser()

chain=prompt1 | llm | parser | prompt2 | llm | parser 

result=chain.invoke({'topic':'image segmentation'})

print(result)