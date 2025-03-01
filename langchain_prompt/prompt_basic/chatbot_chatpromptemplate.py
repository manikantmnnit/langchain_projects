#%%
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    model_name="gpt-4",
    temperature=0.5)

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder("history"),  #history is expected to be a list of tuples, where each tuple represents a message in the format: [("human", "User message"), ("ai", "AI response")]
        ("human", "{question}")
    ]
)

input_data = [{
    "history": [
        ("human", "what's 5 + 2"),
        ("ai", "5 + 2 is 7")],
}]


while True:
    question=input('human:    ')
    if question.lower()=='exit':
        break

    chat_history=input_data[0]['history']

    prompt_input={
        'history':chat_history,
        'question':question
    }
# Format the prompt
    formatted_prompt = prompt.invoke(prompt_input)

    # Get AI response
    response = llm.invoke(formatted_prompt)

    # Print AI response
    print("AI:", response.content)

    # Append new conversation to history
    chat_history.append(("human", question))  # Add human question
    chat_history.append(("ai", response.content))  # Add AI response

    # Update the input_data list
    input_data[0]["history"] = chat_history  # Maintain history for future turns

print(input_data)