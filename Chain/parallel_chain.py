from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1=ChatOpenAI()

model2=ChatCohere(model_name='cohere.command-r-plus')
# model2=ChatOpenAI()

prompt1= PromptTemplate(
    template=" make a short notes on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template=" make  an important question on given on {topic}",
    input_variables=['topic']
)


prompt3=PromptTemplate(
template=" merge the short notes {notes} and important questions {question}  into single documents",
input_variables=['notes','question']
)

parser=StrOutputParser()
notes_chain =prompt1 | model1 | parser
question_chain=prompt2 | model2 | parser

parallel_chain= RunnableParallel(notes=notes_chain, question=question_chain)

merge_chain=prompt3 | model1 |parser

seq_chain=parallel_chain | merge_chain


result=seq_chain.invoke({"topic": "PIL library"})

print(result)

# seq_chain.get_graph.










