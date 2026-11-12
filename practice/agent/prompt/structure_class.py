from pydantic import BaseModel
from model import model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str

# 然后，我们就可以创建智能体并设置结构化输出的格式了。
agent = create_agent(
    model=model,
    system_prompt="你是一个科幻作家，根据用户的要求创建一个太空之都。",
    response_format=CapitalInfo # 设置结构化输出的格式
)

response = agent.invoke(
    {"messages": [HumanMessage(content="月球的首都是什么?")]}
)

city = response['structured_response']

print(f"{city.name}位于{city.location}，是一座{city.vibe}的城市，其主要产业包括{city.economy}。")
