import re
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_template = ChatPromptTemplate(
    [
    ('system', "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human',"{query}"),
    ]
)

chat_history = []
# load chat history and parse message strings into proper Message objects
with open("chat_history.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            continue
        
        # Parse HumanMessage(content="...") and AIMessage(content="...")
        human_match = re.match(r'HumanMessage\(content="(.*)"\)', line)
        ai_match = re.match(r'AIMessage\(content="(.*)"\)', line)
        
        if human_match:
            chat_history.append(HumanMessage(content=human_match.group(1)))
        elif ai_match:
            chat_history.append(AIMessage(content=ai_match.group(1)))


prompt = chat_template.invoke({'chat_history':chat_history, 'query':'where is my refund?'})


print("Generated Prompt:")
print(prompt)