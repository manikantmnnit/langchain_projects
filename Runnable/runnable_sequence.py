from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import dotenv
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt_first=PromptTemplate(
    template="write a paragraph  on {topic} and highlight it's  application in the {domain}",
    input_variables=['topic','domain']
    )


prompt_second=PromptTemplate(
    template=" generate 3 multiple choice question on given {tex} and minimum options should be 4 and all options should be unique. Out of 4 options, only one answer must correct"
)
model=ChatGroq(
        model='llama-3.1-8b-instant',
        temperature=.9,
    )

parser=StrOutputParser()

chain=RunnableSequence(prompt_first,model,parser,prompt_second, model,parser)

result=chain.invoke({
    'topic':'python',
    'domain':'cell analysis of human'})
print(result)