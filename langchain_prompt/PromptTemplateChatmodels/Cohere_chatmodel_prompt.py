
#%%
from langchain_cohere import ChatCohere 
from dotenv import load_dotenv
import os
import pathlib
env_path_name=pathlib.Path.cwd().parent.parent
load_dotenv(dotenv_path=env_path_name / '.env')

#%%
from langchain.prompts import PromptTemplate
from langchain_cohere import ChatCohere
# Create the chain using LangChain's functionality
from langchain.chains import LLMChain

# Define the template with placeholders
prompt = PromptTemplate(
    input_variables=["topic", "location", "time"], 
    template="Tell me about {topic} in {location} during {time}. What is the most important thing to know about {topic} in {location} at {time}?"
)

# Example usage to create a formatted prompt
formatted_prompt = prompt.format(topic="Election result", location="Germany", time="24 Feb 2025")
print(formatted_prompt)

# Define the model (Cohere in this case)
model = ChatCohere(model="command-r")



# Create an LLM chain to combine the prompt template and model
chain = LLMChain(prompt=prompt, llm=model)

# Use the chain to generate a response for a batch of inputs

response = chain.invoke({
    "topic": "History", 
    "location": "Germany", 
    "time": "2022"
})

# Print the response
print(response)