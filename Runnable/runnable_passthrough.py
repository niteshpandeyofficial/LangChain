from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel

load_dotenv()

prompts1=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompts2=PromptTemplate(
    template='explain the following-{text}',
    input_variables=['text']
)

model=ChatOpenAI()
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompts1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompts2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'Cricket'}))

