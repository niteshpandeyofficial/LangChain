from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model =ChatHuggingFace(llm=llm)
schema=[
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]
parsers=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give 3 fact about the {topics} \n {format_instruction}",
    input_variables=['topics'],
    partial_variables={'format_instruction':parsers.get_format_instructions()}
)

chain = template | model | parsers
result=chain.invoke({'topics':'black hole'})
# prompts=template.invoke({'topics':'black hole'})
# result=model.invoke(prompts)
# final_result=parsers.parse(result.content)
# print(final_result)

print(result)








