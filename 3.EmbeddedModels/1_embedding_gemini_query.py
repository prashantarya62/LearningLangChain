from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=32)

# embedding = OpenAIEmbeddings(model="gemini-embedding-001", dimensions=32)


######### Use embed_query for embedding a query ##########
# result = embeddings.embed_query("What is the capital of India?")

######## Use embed_documents for embedding a list of documents ##########
documents = [
    "What is the capital of India?",
    "what is AI?",
    "What is Langchain?"
]
result = embeddings.embed_documents(documents)


print(str(result))
