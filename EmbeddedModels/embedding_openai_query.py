from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

openai_embedding_model = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
result=openai_embedding_model.embed_query('My name is Nitesh')
print(str(result))

