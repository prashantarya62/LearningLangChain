from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=HF_TOKEN,
)

model = ChatHuggingFace(llm=llm)
print(model.invoke("What is capital of India?").content)
