from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from pydantic import BaseModel,Field,StrictStr,EmailStr

load_dotenv()

llm=ChatOpenAI()


# ----------------example 1--------------------------

# class Review(BaseModel):
#     summary:StrictStr
#     sentiment:StrictStr


# structure_llm=llm.with_structured_output(Review)

# result=structure_llm.invoke("""Excellent for straining and filtering liquids, I liked it, I thought it was bigger but for straining it is excellent, thank you for being responsible and punctual, many blessings""" )
# print(result)

#----------------example 2--------------------------


# class Joke(BaseModel):
#     setup:str
#     punchline:str
#     rating:int

# structure_llm=llm.with_structured_output(Joke)
# result=structure_llm.invoke("I asked my dog what 2 minus 2 is. He said nothing!")
# print(result['setup'])


#----------------example 3--------------------------


# # add annotation
class Joke(BaseModel):
    setup: StrictStr=Field(description="The setup of the joke")
    punchline: StrictStr=Field(description="The punchline to the joke")
    rating:  StrictStr=Field(description="How funny the joke is, from 1 to 10")

# structure_llm=llm.with_structured_output(Joke)
# result=structure_llm.invoke("Why did the dog sit in the shade? Because he didn’t want to be a hot dog!")
# print(result['setup'])

#----------------example 4--------------------------
# multiple task  at a time
# using abatch

# class Joke(TypedDict):
#     setup: Annotated[str,"The setup of the joke"]
#     punchline: Annotated[str,"The punchline to the joke"]
#     rating: Annotated[int,"How funny the joke is, from 1 to 10"]

# messages=[
#         [{'role':'user','content':' Why don’t skeletons fight each other? Because they don’t have the guts!'}],
#         [{'role':'user','content':' Why did the math book look sad?It had too many problems!'}],
#         [{'role':'user','content':' Why don’t eggs tell jokes? Because they might crack up!'}]
#       ] 
# structure_llm=llm.with_structured_output(Joke)

# # Define the async function
# import asyncio
# async def main():
   
#     structure_llm = llm.with_structured_output(Joke)

#     # Using abatch to process multiple requests
#     result = await structure_llm.abatch(messages)

#     # Print the results
#     for res in result:
#         print(res)

# # Run the async function using asyncio.run()
# asyncio.run(main())


# load json schema


class player(BaseModel):
    title:str
    type:str
    properties:list[str]
    name:str
    email:EmailStr

