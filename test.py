# import langchain
# import os
# # from langchain_google_genai import genai
# from dotenv import load_dotenv  
# load_dotenv()
# print("LangChain version:", langchain.__version__)
# print('GOOGLE_API_KEY set:', bool(os.environ.get('GOOGLE_API_KEY')))
# models = genai.list_models()




from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from dotenv import load_dotenv      




########WE SET THE HF CACHE DIRECTORY LOCATION HERE IF NEEDED##########
# import os
# os.environ["HF_HOME"] = "D:/HF_CACHE"

llm = HuggingFaceEndpoint(
    repo_id="naver-clova-ix/donut-base-finetuned-docvqa", 
    task="image-to-text",
)   


# model = ChatHuggingFace(llm=llm) 

# model_response = model.invoke("What is capital of india?")
# print(model_response.content)

