from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model =ChatHuggingFace(llm=llm)
parsers=JsonOutputParser()
#1st prompts ---Details reports
template=PromptTemplate(
    template="Give me the name,age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parsers.get_format_instructions()}
)

#recommended way
chain = template | model | parsers

# Traditional Ways
# prompts =template.format()
# result=model.invoke(prompts)
# final_result=parsers.parse(result.content)
# print(final_result)

result=chain.invoke({})
print(result)






