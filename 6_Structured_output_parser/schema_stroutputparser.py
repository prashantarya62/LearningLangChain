from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
from dotenv import load_dotenv      
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema



########WE SET THE HF CACHE DIRECTORY LOCATION HERE IF NEEDED##########
# import os
# os.environ["HF_HOME"] = "D:/HF_CACHE"
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it", 
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="The first fact about the topic"), 
    ResponseSchema(name="fact_2", description="The second fact about the topic"),
    ResponseSchema(name="fact_3", description="The third fact about the topic"),
] 

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.invoke({'topic':"black hole"})

result = model.invoke(prompt)

final_result = parser.parse(result)
print("________________________________")
print(final_result)  