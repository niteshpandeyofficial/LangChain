from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

from dotenv import load_dotenv
import os
load_dotenv()

class Person(BaseModel):
    name:str =Field(description="Person's name")
    age:int =Field(gt=18,description="Person's age")
    city:str =Field(description="Person's city")


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model =ChatHuggingFace(llm=llm)

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template="Generate name,age and city of fictional {place} person \n "
             "{format_instruction}",
    input_variables=['palce'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain=template|model|parser
final_result=chain.invoke({'place':'pakistani'})
# prompts=template.invoke({'place':'indian'})
#
# result=model.invoke(prompts)
# final_result=parser.parse(result.content)
print(final_result)









