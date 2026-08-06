from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
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

prompt1=template1.invoke({'topic':'black whole'})
result = model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)

print(result.content)
print(result1.content)




