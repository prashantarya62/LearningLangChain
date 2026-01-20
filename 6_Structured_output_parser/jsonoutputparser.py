from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from dotenv import load_dotenv      
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser



########WE SET THE HF CACHE DIRECTORY LOCATION HERE IF NEEDED##########
# import os
# os.environ["HF_HOME"] = "D:/HF_CACHE"
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it", 
    task="text-generation",
)

model = ChatHuggingFace(llm=llm) 

parser = JsonOutputParser()
template1 = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({'topic':"black hole"})
print("________________________________")
print(result.content)

