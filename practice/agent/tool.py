import os
from dotenv import load_dotenv
from langchain.tools import tool  # ← 补上这一行
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

load_dotenv()


# 2.定义工具，基础版，通过注释描述工具
@tool
def getWeather(location: str) -> str:
    """
    Get the weather in a given location.
    Args:
        location: city name or coordinates
    """
    return f"Current weather in {location} is sunny"


model = init_chat_model(
    model=os.getenv("SENSENOVA_MODEL"),
    model_provider="openai",
    base_url=os.getenv("SENSENOVA_BASE_URL"),
    api_key=os.getenv("SENSENOVA_API_KEY"),
)

# 3.定义Agent
agent = create_agent(model=model, tools=[getWeather])

# 4.调用模型
print("🚀 正在调用大模型...")
response = agent.invoke(
    {"messages": [{"role": "user", "content": "杭州今天天气如何?"}]}
)

# 5.打印结果
print(response)
