from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder

from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    model_name="gpt-4",
    temperature=0.5)


# # create a infinite loop until user wants exit
# while True:
#     user_input=input('you:  ')
#     if user_input.lower() == 'exit':
#         break
#     result=llm.invoke(user_input)
#     print('AI: {result.content}')

# major problem is that chatbot never remember the previous chat
# Initialize chat history
chat_history = []

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':  # Exit condition
        break

    chat_history.append(user_input)  # Store user input
    result = llm.invoke(chat_history)  # Invoke LLM model
    ai_response = result.content
    chat_history.append(ai_response)  # Store AI response
    print(f'AI: {ai_response}')

print(chat_history)

