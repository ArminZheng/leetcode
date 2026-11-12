## 记忆管理策略 - 总结消息
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from model import model

# 初始化checkpointer
checkpointer = InMemorySaver()
# 初始化中间件
middleware = SummarizationMiddleware(
    model=model, # 总结完全不需要那么聪明的模型。你可以给中间件传一个便宜的小模型
    trigger=("messages", 3),  #  触发时机，当消息数超过3时，进行总结
    keep=("messages", 1),  #  保留的会话数，超过2条
)

# 创建agent
agent = create_agent(
    model=model,
    middleware=[middleware],
    checkpointer=checkpointer,
)

config: RunnableConfig = {"configurable": {"thread_id": "1"}}
# 制造长会话历史

from langchain.messages import HumanMessage

agent.invoke({"messages": [HumanMessage(content="你好，我是虎哥.")]}, config)
agent.invoke({"messages": [HumanMessage(content="我最喜欢的运动是乒乓")]}, config)
agent.invoke({"messages": [HumanMessage(content="我最喜欢的动物是猫猫")]}, config)
# 测试效果
final_response = agent.invoke({"messages": [HumanMessage(content="你还记得我吗？")]}, config)


for message in final_response["messages"]:
    message.pretty_print()
