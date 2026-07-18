from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_anthropic_model = ChatAnthropic(model='claude-haiku-4-5-20251001')
result=chat_anthropic_model.invoke("What is the capital of India")
# print(result)
print(result.content)