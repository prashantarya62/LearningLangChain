from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# load_dotenv()

llm = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2" 
)

documents = [
    "Virat kohli is an Indian cricketer known for his aggressive batting style.",
    "Sachin tendulkar is an Indian cricketer known for his record-breaking performance.",
    "MS Dhoni is an Indian cricketer known for his calm demeanor and leadership skills.",
    "Rohit Sharma is known for his elegant batting and ability to score big hundreds.",
    "Jasprit Bumrah is known for his unique bowling action and yorkers."
]

query = "tell me about virat kohli"

doc_embeddings = llm.embed_documents(documents)
query_embedding = llm.embed_query(query)
similarities = cosine_similarity(
    [query_embedding],
    doc_embeddings
).flatten()

# print("Similarities:", similarities)

print("Similarities:", list(enumerate(similarities)))

print("sorted Similarities:", sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1])


index, score = sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1]
print(f"Most similar document to the query: '{documents[index]}' with a similarity score of {score}")