from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1=PromptTemplate(
    template="write the tweet for {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="write the linked post for {topic}",
    input_variables=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()

chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result=chain.invoke({'topic':'AI'})
print(result)


