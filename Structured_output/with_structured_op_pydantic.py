from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel,Field
from typing import Optional, Literal

BASE_DIR = Path(__file__).resolve().parent.parent
file_path=BASE_DIR / "Structured_output" / "reviews.txt"
load_dotenv()
model=ChatOpenAI()

class Review(BaseModel):
    key_themes:list[str] = Field(description="Write down all the key themes discussed in the review in the list")
    summary:str =Field(description="A brief summary of the review")
    sentiment: Literal["pos","neg"] =Field(description="Return sentiment of review either Positive, Negative, or Neutral")
    pros: Optional[list[str]]=Field(default=None,description="Write down all the pros if available in the review")
    cons: Optional[list[str]]=Field(default=None,description="Write down all the cons if available in the review")
    reviewer:Optional[str]=Field(default=None,description="Write down the reviewer name")

structured_op=model.with_structured_output(Review)
with open(file_path,"r") as f:
    content=f.read()

# with open("D:\\LangChain_Models\\Structured_output\\reviews.txt",'r') as f:
#     content=f.read()


result=structured_op.invoke(content)
# result=structured_op.invoke("""The hardware is great ,but the software feel bloated. There are too many pre-installed
#                                 apps that i can't remove.Also the UI looks outdated compare to other brands.
#                                 Hoping for software update to fix this.""")

print(result)