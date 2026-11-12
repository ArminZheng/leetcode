import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

# 初始化checkpointer
checkpointer = SqliteSaver(sqlite3.connect("checkpoint.db", check_same_thread=False))
# 自动建表
checkpointer.setup()


from langchain.agents import create_agent
from model import model

# 创建agent
agent = create_agent(
    model,
    checkpointer=checkpointer
)

from langchain.messages import HumanMessage

from langchain_core.runnables import RunnableConfig
# 设定thread_id，作为会话标识
config: RunnableConfig = {"configurable": {"thread_id": "thread_1"}}

# 第一次调用，告知AI我的信息
response = agent.invoke(
    {"messages": [HumanMessage(content="你好，我叫虎哥，我最喜欢暹罗猫。")]},
    config # 调用时添加thread_id，区分不同会话
)

print(response)

# 第二次调用，询问我的信息，这次带上thread_id，唤起记忆
response = agent.invoke(
    {"messages": [HumanMessage(content="我最喜欢的动物是什么？")]},
    config # 调用时添加thread_id
)

print(response)

