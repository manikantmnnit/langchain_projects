from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
     model_name="gpt-4",
     temperature=0
)

result=llm.invoke('Write 2 sentences  on Children')
print(result.content)