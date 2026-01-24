# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# from langchain.chains import LLMChain
# # from langchain_core.ch

# load_dotenv()


# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# prompt = PromptTemplate(
#     template="Suggest a catchy blog title about {topic}.",      
#     input_variables=['topic'],
# )

# chain = LLMChain(model=model, prompt=prompt)
# topic = input("Enter a topic: ")
# result = chain.run(topic=topic)
# print("________________________________")
# print(result)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}.",
    input_variables=["topic"],
)

chain = prompt | model | StrOutputParser()

topic = input("Enter a topic: ")
result = chain.invoke({"topic": topic})

print("________________________________")
print(result)
