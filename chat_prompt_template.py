from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


chat_template = ChatPromptTemplate(
    [
('system', "You are a helpful {domain} expert."),
('human'," Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({'domain': 'technology', 'topic': 'machine learning'})

print("Generated Prompt:")
print(prompt)