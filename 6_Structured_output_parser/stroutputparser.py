from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from dotenv import load_dotenv      
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser




########WE SET THE HF CACHE DIRECTORY LOCATION HERE IF NEEDED##########
# import os
# os.environ["HF_HOME"] = "D:/HF_CACHE"
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it", 
    task="text-generation",
)

model = ChatHuggingFace(llm=llm) 

template1 = PromptTemplate(
    template="Give me a detailed explanation of the topic: {topic}",
    input_variables=["topic"]   
)


template2 = PromptTemplate(
    template="write a 5 lines summary on the following text. /n {text}",
    input_variables=["text"]   
)

prompt1 = template1.invoke({'topic':"black hole"})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)
 

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':"black hole"})
print("________________________________")
print(result)



