from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate, HumanMessagePromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain.chains import ConversationChain
from tool import getWeather
from langchain_core.messages import HumanMessage

chat = ChatZhipuAI(
    model="glm-4",
    # model="glm-4",
    temperature=0.5,
)


tool = [getWeather]

agent_excutor = create_react_agent(chat, tools=tool)

response = agent_excutor.invoke({"messages": [HumanMessage(content="厦门天气")]})
print(response)

print("*"*40)

response = agent_excutor.invoke({"messages": [HumanMessage(content="北京天气")]})

print(response)
