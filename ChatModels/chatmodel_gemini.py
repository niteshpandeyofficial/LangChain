from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

google_gemini_model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')
result=google_gemini_model.invoke('What is the capital of india')
# print(result)
print(result.text)
