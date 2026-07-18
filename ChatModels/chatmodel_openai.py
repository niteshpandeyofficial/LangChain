from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_openai_model = ChatOpenAI(model='gpt-4')
# temperature=0-2 --control the randomness of a language models output,
# max_completion_tokens=0-any number(restrict the no of token in response)
result=chat_openai_model.invoke("What is the capital of India")

print(result.content)


