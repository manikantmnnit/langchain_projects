from langchain_cohere import ChatCohere
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

import os

model1=ChatCohere(model_name='cohere.command-r-plus',cohere_api_key=os.getenv("COHERE_API_KEY"))
# model1=ChatOpenAI()


parser1=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Provide the sentiment of the given feedback."
    )

parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template=(
        "Analyze the sentiment of the following feedback.\n"
        "{format_instruction}\n\n"
        "Feedback: {feedback}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)


classifier_chain=prompt1 |model1 | parser2


positive_prompt=PromptTemplate(
    template="Write an appropriate response to this positive feedback {feedback}",
    input_variables=['feedback']
)

negative_prompt=PromptTemplate(
    template="Write an appropriate response to this negative feedback {feedback}",
    input_variables=['feedback']
)

branch_chain=RunnableBranch( 
    (lambda x:x.sentiment=='Positive', positive_prompt | model1 | parser1),
    (lambda x:x.sentiment=='Negative', negative_prompt | model1 | parser1),
    RunnableLambda(lambda x: "could find a sentiment")

)


final_chain=classifier_chain |branch_chain


result=final_chain.invoke({'feedback':" this is really good product in AI domain. I think it will change the world's working style"})
print(result)

