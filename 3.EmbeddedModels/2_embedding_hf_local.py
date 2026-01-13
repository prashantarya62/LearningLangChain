from langchain_huggingface import HuggingFaceEmbeddings


llm = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2" 
)

documents = [
    "What is the capital of India?",
    "what is AI?",
    "What is Langchain?"
]
result = llm.embed_documents(documents)
print(str(result))