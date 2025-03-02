from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to read and format chat history
def load_chat_history(file_path):
    chat_history = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("Human (Patient):"):
                chat_history.append(("human", line.replace("Human (Patient):", "").strip()))
            elif line.startswith("AI (Doctor):"):
                chat_history.append(("ai", line.replace("AI (Doctor):", "").strip()))
    return chat_history

# Load chat history
chat_history = load_chat_history('langchain_prompt/prompt_basic/chat_history_medical.txt')

# Create chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a compassionate doctor, providing information and support to a patient regarding their cancer diagnosis."),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{patient_input}')  # Correct message type
])

# Initialize the LLM once
llm = ChatOpenAI()

while True:
    patient_input = input('Human (Patient): ')
    if patient_input.lower() == 'exit':
        break

    # Update chat history
    chat_history.append(('human', patient_input))  # Correct format

    # Prepare input for the AI
    chat_input = chat_template.invoke({
        'history': chat_history,
        'patient_input': patient_input  # Correct variable name
    })

    # Get AI response
    result = llm.invoke(chat_input)

    # Store AI response in history
    chat_history.append(('ai', result.content))  # Store AI response correctly

    print(f"AI (Doctor): {result.content}")

print(chat_history)  # Print final chat history
