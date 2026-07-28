from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["HF_HOME"] = "D:/huggingface_cache"
# TinyLlama/TinyLlama-1.1B-Chat-v1.0 not supported by huggingface now.
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.2,
        max_length=100,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("what is the capital of India")
print(response)