from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompts1 = PromptTemplate(
    template='Generate the details reports of {topic}',
    input_variables=['topic']
)

prompts2 = PromptTemplate(
    template='Generate the 5 pointer summary of text \n {text}',
    input_variables=['text']
)
model=ChatOpenAI()
parser = StrOutputParser()

chain = prompts1 | model | parser | prompts2 | model | parser
result=chain.invoke({'topic':'Unemployment'})
print(result)

chain.get_graph().print_ascii()



