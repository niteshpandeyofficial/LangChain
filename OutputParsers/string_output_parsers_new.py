from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model =ChatHuggingFace(llm=llm)

#1st prompts ---Details reports
template1=PromptTemplate(
    template="write a details reports on {topic}",
    input_variables=['topic']
)
#2nd prompts--->prompts summary
template2=PromptTemplate(
    template="write a 5 line summary on the following text./n {text}",
    input_variables=['text']
)


parser =StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)



