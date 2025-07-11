from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatZhipuAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chat = ChatZhipuAI(
    model="glm-4",
    # model="glm-4",
    temperature=0.5,
)

conversation = ConversationChain(
    llm=chat,
    verbose=True,
    memory=ConversationBufferMemory()
)
print(conversation.predict(input="并发高的项目应该注意什么"))

print("****")

print(conversation.predict(input="我上一句说的什么"))