from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,List

load_dotenv()

llm=ChatOpenAI()


#----------------example 1--------------------------

# class Review(TypedDict):
#     summary:str
#     sentiment:str


# structure_llm=llm.with_structured_output(Review)

# result=structure_llm.invoke("""Excellent for straining and filtering liquids, I liked it, I thought it was bigger but for straining it is excellent, thank you for being responsible and punctual, many blessings""" )
# print(result)

#----------------example 2--------------------------


# class Joke(TypedDict):
#     setup:str
#     punchline:str
#     rating:int

# structure_llm=llm.with_structured_output(Joke)
# result=structure_llm.invoke("I asked my dog what 2 minus 2 is. He said nothing!")
# print(result['setup'])


#----------------example 3--------------------------


# # add annotation
# class Joke(TypedDict):
#     setup: Annotated[str,"The setup of the joke"]
#     punchline: Annotated[str,"The punchline to the joke"]
#     rating: Annotated[int,"How funny the joke is, from 1 to 10"]

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


# 
# ------------------------Example 5----------------------

# 
# from typing import Annotated
# from dataclasses import dataclass

# @dataclass
# class ValueRange:
#     lo: int
#     hi: int
# def wheatherResponse(TypeDict):
#     location:Annotated[str,"Name of place where you want to find weather predtion"]
#     Temperature: Annotated[float,ValueRange(-20,55), " fetch the temperature in degree Celcious"]
#     Wind_speed:Annotated[float,'Speed of wind (KM per hour)']
#     condition:Annotated[str, "windy","Sunny","Cloudy","cold","raining",'fog']
#     Conclusion:Annotated[str,"Brief summary about wheather"]


# llm_structured=llm.with_structured_output(wheatherResponse)

# result=llm_structured.invoke("""Today, March 6, 2025, Minneapolis is experiencing cloudy conditions with a temperature around 27°F (-3°C). After a significant winter storm earlier this week, which brought heavy snowfall and blizzard conditions to the region, the city is now seeing more typical March weather. Forecasts predict a high of 34°F (1°C) today, with mostly sunny skies and a light southwesterly breeze. 
# This marks a return to seasonable temperatures following the recent severe weather events.""")
# print(result)

# ----------------------example -6--------------------------



# class Patient(TypedDict):
#     Name: str
#     Age:  int
#     Disease: str
#     symptoms: list[str]
#     precautions:list[str]

# # patient:Patient={'Name':'mkk',
# #                 'age':25,
# #                 'Disease':'Hypertenstion',
# #                 'symtoms':['headache','chest_pain','dizziness','loss_of_balance','lack_of_concentration'],
# #                 'precautions':['meditation', 'salt baths',' reduce stress', 'get proper sleep']}

# structured_llm=llm.with_structured_output(Patient)
# result=structured_llm.invoke(''' MKK, a 25-year-old patient diagnosed with hypertension, experiences symptoms 
#                              such as headache, chest pain, dizziness, loss of balance, and lack of concentration. 
#                              To manage the condition, it is recommended to follow precautions like meditation, 
#                              salt baths, stress reduction, and getting proper sleep.''')

# print(result)


# ----------------------example 7--------------------------

from typing import Literal, Annotated, Optional
query= 'Capital of Inida is ......'
class APIResponse(TypedDict):
    status: Literal['success','error']
    data: Optional[dict]
    message: Optional[str]

def process_api_request(query:str) ->APIResponse:
    llm=ChatOpenAI().with_structured_output(APIResponse)
    return llm.invoke(f"Process this request {query}")

print(process_api_request(query=query))









