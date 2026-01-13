from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain import chains

st.header("Prompt Template Example")


# user_input = st.text_input("Enter your prompt:")

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


paper_input = st.selectbox( "Select a paper topic:", 
    ("Artificial Intelligence", "what is numpy in Machine Learning", "Natural Language Processing", "Computer Vision")
)

style_input = st.selectbox( "Select Explanation style:",
    ("Simple", "Detailed", "Technical", "Layman")
)

length_input = st.selectbox( "Select Explanation length:",
    ("Short", "Medium", "Long")
)   

template = load_prompt("template.json")




if st.button("Generate Output"):
    print("Generating output...")
    # print(f"User Input: {user_input}")
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)
