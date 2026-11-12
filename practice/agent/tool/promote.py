from pydantic import BaseModel, Field
from model import model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

# Agent回答内容引用的网页信息
class Reference(BaseModel):
    title: str = Field(description="The title of the web page cited in the answer")
    url: str = Field(description="The url of the web page cited in the answer")

# Agent的回答内容
class AnswerInfo (BaseModel):
    answer: str = Field(description="The final answer for user")
    reference: list[Reference] = Field(description="The web pages cited in the answer")

from langchain_core.tools import StructuredTool

def isSearch(content: str) -> bool:
    print("hah, " + content)
    return True

should_search = StructuredTool.from_function(
    func=isSearch,
    name="should_search",
    description="是否应该联网搜索",
)
    
# 创建智能体，使用预定义工具tavily
agent = create_agent(
    model=model,
    tools=[should_search],
    system_prompt="你是一个智能助手，你使用网络搜索工具来解决用户问题。",
    response_format=AnswerInfo
)

# 调用agent
response = agent.invoke(
    {"messages": [HumanMessage(content="蒸蚌是什么梗？")]},
)

# 获取结构化输出
print(response['structured_response'])
for message in response['messages']:
    message.pretty_print()
