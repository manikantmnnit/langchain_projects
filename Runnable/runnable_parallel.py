from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import dotenv
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from transformers import pipeline
from langchain_core.output_parsers import JsonOutputKeyToolsParser

load_dotenv()

prompt1 = PromptTemplate(
    template='''
    Perform the following tasks related to the topic: "{topic}"
    
    1️⃣ **YouTube Links**:
       - Provide several YouTube links that cover the topic. Ensure these are relevant and useful.

    2️⃣ **Books**:
       - List some books that offer in-depth coverage of the topic. Include titles and authors.

    3️⃣ **Online Courses**:
       - Suggest a few online courses or platforms that feature this topic in their syllabus. Mention the course title and platform.

    Please ensure the information is accurate and relevant. Only provide the requested details without any extra commentary.
    ''',
    input_variables=['topic']
)

model=ChatGroq(
        model='llama-3.1-8b-instant',
        temperature=.9,
    )

parser=StrOutputParser()

chain=prompt1 | RunnableParallel(
            {"youtube link": model |parser,
             "book_name": model |parser,
              "online course list": model | parser
              }
        )

result=chain.invoke({'topic':'Computer vision in medical domain'})
print(result)

