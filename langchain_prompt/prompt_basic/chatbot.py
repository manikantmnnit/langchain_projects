from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder

from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    llm='gpt-4',
    temperature=0.5)

# create a infinite loop until user wants exit
while True:
    user_input=input('you:  ')
    if user_input=='Exit':
        break
    result=llm.invoke(user_input)

