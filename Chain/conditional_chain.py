from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompts =PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback} '
             '\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}

)

prompts1 =PromptTemplate(
    template='Write an appropriate response to this positive feedback\n {feedback} ',
    input_variables=['feedback']
)

prompts2 =PromptTemplate(
    template='Write an appropriate response to this negative feedback\n {feedback} ',
    input_variables=['feedback']
)

model =  ChatOpenAI()
classified_chain = prompts | model | parser2
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompts1 | model | parser),
             (lambda x:x.sentiment == 'negative', prompts2 | model | parser),
            RunnableLambda(lambda x : "Could not find the sentiment")
)

final_chain= classified_chain| branch_chain
final_result=final_chain.invoke({'feedback':'This is the terrible smartphone'})
print(final_result)

branch_chain.get_graph().print_ascii()
# result=classified_chain.invoke({'feedback':'This is the terrible smartphone'}).sentiment
# print(result)

