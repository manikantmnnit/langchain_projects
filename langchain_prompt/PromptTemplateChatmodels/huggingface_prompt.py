#%%
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import pathlib
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
#%%
load_dotenv()
repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

llm = HuggingFaceEndpoint(  
        repo_id=repo_id,  
        task="Text Generation",  
        max_new_tokens=512,  
        do_sample=False  
)

model=ChatHuggingFace(llm=llm,verbose=True)


# Define a simple prompt template
template = "Translate the following text to {language}: {text}"

prompt_template = PromptTemplate(
    input_variables=['language', 'text'],
    template=template
)

# Formatting the template with actual values
formatted_prompt = prompt_template.format(
    language='Hindi',
    text='Where are you going?'
    )


chain = LLMChain(prompt=prompt_template, llm=model)

# Use the chain to generate a response for a batch of inputs

response = chain.invoke({
   'language': 'Hindi',
    'text':'Where are you going?'
})

# Print the response
print(response)