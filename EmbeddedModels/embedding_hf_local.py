from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["EMBEDDING_HF_HOME"] = "D:/embedded_huggingface_cache"
embedding_hf = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
documents=['Delhi is capital of India',
           'Lucknow is capital of Gorakhpur',
           'kolkata is capital of West Bangal']

# text= 'Python is very simple language'
# result=embedding_hf.embed_query(text)

result=embedding_hf.embed_documents(documents)
print(str(result))