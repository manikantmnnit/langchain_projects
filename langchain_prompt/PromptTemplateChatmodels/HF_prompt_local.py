from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import pathlib
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
# use huggingface pipline
#%%
load_dotenv()
from langchain_huggingface import HuggingFacePipeline

from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='meta-llama/Llama-2-7b-chat-hf',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=1.5,
        max_new_tokens=100
    )
)

model=ChatHuggingFace(llm=llm,verbose=True)


# Define a simple prompt template
template = "Translate the following text to {language}: {text}"

prompt_template = PromptTemplate(
    input_variables=['language', 'text'],
    template=template
)

# # Formatting the template with actual values
# formatted_prompt = prompt_template.format(
#     language='Hindi',
#     text='Where are you going?'
#     )


chain = LLMChain(prompt=prompt_template, llm=model)

# Use the chain to generate a response for a batch of inputs

response = chain.invoke({
   'language': 'Hindi',
    'text':'Where are you going?'
})

# Print the response
print(response)

# %%
ChatHuggingFace()