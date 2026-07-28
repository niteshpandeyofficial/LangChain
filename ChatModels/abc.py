import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

completion = client.chat.completions.create(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)