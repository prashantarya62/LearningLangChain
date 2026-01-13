import langchain
import os
# from langchain_google_genai import genai
from dotenv import load_dotenv  
load_dotenv()
print("LangChain version:", langchain.__version__)
print('GOOGLE_API_KEY set:', bool(os.environ.get('GOOGLE_API_KEY')))
# models = genai.list_models()
