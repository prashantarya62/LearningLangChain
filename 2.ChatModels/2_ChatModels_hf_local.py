from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv      




########WE SET THE HF CACHE DIRECTORY LOCATION HERE IF NEEDED##########
# import os
# os.environ["HF_HOME"] = "D:/HF_CACHE"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
        )
)   

model = ChatHuggingFace(llm=llm) 

model_response = model.invoke("What is capital of india?")
print(model_response.content)

