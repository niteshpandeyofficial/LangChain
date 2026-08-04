from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
from typing import TypedDict ,Annotated,Optional

BASE_DIR = Path(__file__).resolve().parent.parent
file_path=BASE_DIR / "Structured_output" / "reviews.txt"
load_dotenv()
model=ChatOpenAI()

class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the key themes discussed in the review in the list"]
    summary: Annotated[str,"A brief summary of the review"]  #annoted dict
    sentiment: Annotated[str,"Return sentiment of review either Positive, Negative, or Neutral"]
    pros: Annotated[Optional[list[str]],"Write down all the pros if available in the review"]
    cons: Annotated[Optional[list[str]],"Write down all the cons if available in the review"]
    reviewer:Annotated[str,"Write down the reviewer name"]

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