from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnablePassthrough

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import pathlib
import os


load_dotenv()

llm=ChatGroq(
        model='llama-3.1-8b-instant',
        temperature=.9,
    )

file_path=pathlib.Path.cwd()/'Document_loader'

file_name='DNA_RNA'


def doc_extract(file_path,file_name):
    loader=TextLoader(os.path.join(str(file_path), f"{file_name}.txt"),encoding='utf-8')
    documents=loader.load()
    return documents[0].page_content



prompt=PromptTemplate(
    template=''' '
    'summarize the given {text} in 100 lines '
    dont extract anything from internet source'
    'provide me summary in bullet form''' ,
    input_variables=['text']
)

parser=StrOutputParser()

input_dict = {
    "file_path": pathlib.Path.cwd()/'Document_loader',
    "file_name": 'DNA_RNA'
}

# Chain construction
chain = (
    RunnableLambda(lambda x: doc_extract(x["file_path"], x["file_name"]))  
    | prompt     
    | llm     
    | StrOutputParser()
    )


# Invoke the chain with parameters
result = chain.invoke(input_dict)

print(result)

