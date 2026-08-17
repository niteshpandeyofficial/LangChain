from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm_openai = OpenAI(model='gpt-3.5-turbo-instruct')

template =PromptTemplate(
    template="Suggest best reading books for {topic}",
    input_variables=['topic']
)

topic= input("Enter your topic: ")
formatted_topic = template.format(topic=topic)
books_det=llm_openai.invoke(formatted_topic)

print(f"Best books for asked topic is:{books_det}")