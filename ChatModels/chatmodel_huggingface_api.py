from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

# TinyLlama/TinyLlama-1.1B-Chat-v1.0 not supported by huggingface now.
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm,)
response = model.invoke("what is the capital of India")
print(response)