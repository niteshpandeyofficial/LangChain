from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
file_path=BASE_DIR / "Runnable" / "testing.txt"

#Loads the documents
loader = TextLoader(file_path)
document = loader.load()

#split the documents
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=text_splitter.split_documents(document)

#convert text into embedding & store in FAISS
vectorstore=FAISS.from_documents(docs,OpenAIEmbeddings())

# Create a retriever(Fetches relevant documents)
retriever=vectorstore.as_retriever()

# Manually retrieve the relevant document
query="What are the key takeaway from this document?"
relevant_docs=retriever._get_relevant_documents(query)

#Combine retrieve text into single prompts
retrieved_text="\n".join([doc.page_content for doc in relevant_docs])

#initialize the LLM
llm=OpenAI(model='gpt-3.5-turbo-instruct')

#manually pass retrieve text to llm
prompt="Based on the following text,answer the question:{query}\n\n{retrieved_text}"
answer=llm.invoke(prompt)
print(f"Answer: {answer}")

