from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat templates
chat_template=ChatPromptTemplate([
    ('system','You are a helpful cusomter agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')]
)

chat_history=[]

#load the chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create prompts
prompt=chat_template.invoke({'chat_history':chat_history,'query':'what about my refund'})
print(prompt)



