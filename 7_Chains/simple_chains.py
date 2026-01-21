from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()


prompt = PromptTemplate(
    template="Give me 5 interesting facts about {topic}.",
    input_variables=['topic'],
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':"langchain framework"})
print("________________________________")   
print(result)

chain.get_graph().print_ascii()
