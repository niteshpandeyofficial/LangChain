from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert!'),
    ('human','Explain in simple term ,what is {topic}')
]
)

prompt=chat_template.invoke({'domain':'cricket','topic':'wide ball'})
print(prompt)