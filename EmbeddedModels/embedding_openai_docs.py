from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_docs=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
documents=['Python is high level language','C/C# is low level language','Oracle is Relational DB','Dynamo DB is nosql DB']
result=embedding_docs.embed_documents(documents)

print(str(result))