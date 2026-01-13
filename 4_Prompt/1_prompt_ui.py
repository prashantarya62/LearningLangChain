
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

import streamlit as st
from langchain.prompts import PromptTemplate

st.header("Prompt Template Example")


user_input = st.text_input("Enter your prompt:")

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
        )
)   


model = ChatHuggingFace(llm=llm) 

paper_input = st.selectbox( "Select a paper topic:", 
    ("Artificial Intelligence", "Machine Learning", "Natural Language Processing", "Computer Vision")
)

style_input = st.selectbox( "Select Explanation style:",
    ("Simple", "Detailed", "Technical", "Layman")
)

length_input = st.selectbox( "Select Explanation length:",
    ("Short", "Medium", "Long")
)   


#templete
template = """Explain the topic of {paper} in a {style} manner with {length} length."""

if st.button("Generate Output") and user_input:
    print("Generating output...")
    print(f"User Input: {user_input}")
    model_response = model.invoke(user_input)
    st.write(model_response)
