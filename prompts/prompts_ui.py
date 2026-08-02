from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()

st.header("Research Tool")
# user_input=st.text_input("Please enter your prompts:")

model=ChatOpenAI()

paper_input=st.selectbox("Select Research Paper Name",["Attention Is All You Need",
                                                       "BERT:Pre-training of Deep Bidirectional Transformers",
                                                       "GPT-3:Language Models are Few-Shot Learners",
                                                       "Diffusion Models Beat GANs on Image Sythesis"])

style_input=st.selectbox("Select Explanation Style",["Beginner-Friendly","Technical",
                                                     "Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["Short(1-2 paragraphs)",
                                                       "Medium(3-5 paragraphs)","Long(Detailed Explanation)"])
template=PromptTemplate(
    template="""
    Please summarized the research paper titled "{paper_input}" with the following specifications:
    Explanation style:{style_input}
    Explanation length:{length_input}
    1. Mathematical details:
        - Include relevant mathematical equations if present in the paper.
        - Explain the mathematical concept using simple,intuitive code snippet where applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper, respond with : "Insufficient Information 
    available" instead of guessing.
    Ensure the summary is clear , accurate, and aligned with the provided style and lenght.
    """,
    input_variables=['paper_input','style_input','length_input']
)

#fill the place holder
prompts=template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})


if st.button('Summarize'):
    result=model.invoke(prompts)
    st.write(result.content)
