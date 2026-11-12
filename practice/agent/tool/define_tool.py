from model import model
from langchain.tools import tool
from pydantic import BaseModel, Field
from typing import Literal

# 智能体在工作时，需要将函数的名称、输入、作用传递给大模型，默认情况下这些信息的来源是：​
# 工具名称：函数名​
# 工具输入：函数入参​
# 工具作用：函数的注释
@tool("square_root")
def tool1(x: float) -> float:
    """Calculate the square root of a number"""
    return x ** 0.5

# 我们可以通过tool装饰器来覆盖上述信息：
@tool("square_root", description="Calculate the square root of a number")
def tool2(x: float) -> float:
    return x ** 0.5

# 如果要覆盖工具的入参信息则会复杂很多，我们要借助于Pydantic或JSON约束。
# 例如一个查询天气的tool
class WeatherInput(BaseModel):
    """查询天气的输入参数."""
    location: str = Field(description="City name or coordinates")
    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius",
        description="Temperature unit preference"
    )
    include_forecast: bool = Field(
        default=False,
        description="Include 5-day forecast"
    )

# 定义一个查询天气的tool
@tool(args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result

"""
在LangChain中，作为工具的函数有两个保留的参数名，你的自定义参数不能与之重复！他们是：
- config：用来传递运行时配置
- runtime：用来传递运行时上下文

"""

from langchain.agents import create_agent
from langchain.messages import HumanMessage

# 创建智能体，并添加工具
agent = create_agent(
    model=model,
    tools=[tool1, get_weather],
    system_prompt="你是一个智能助手，你使用工具来解决用户问题。"
)

# 调用智能体
for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="467的平方根是多少?")]},
    stream_mode="messages"
):
    print(token.content, end="", flush=True)
    

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="北京和杭州接下来几天天气如何?")]},
    stream_mode="messages"
):
    print(token.content, end="", flush=True)
