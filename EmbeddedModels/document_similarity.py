from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding =OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

user_query='tell me about the Sachin'
docs_embeddings=embedding.embed_documents(documents)
query_embed=embedding.embed_query(user_query)
score=cosine_similarity([query_embed],docs_embeddings)[0]

index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(f"user_query:{user_query}")
print(f"Result:{documents[index]}")
print(f"Similarity score:{score}")




