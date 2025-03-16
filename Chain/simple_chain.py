from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
    template="Tell me about five tools about{topic} in python library",
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

chain =prompt |model | parser

result=chain.invoke({"topic":"Image Segmentation"})

print(result)

