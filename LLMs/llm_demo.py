from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv(verbose=True)

llm_openai = OpenAI(model='gpt-3.5-turbo-instruct')
result=llm_openai.invoke("What is the capital of India")
print(result)

