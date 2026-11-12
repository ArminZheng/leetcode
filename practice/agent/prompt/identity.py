from model import model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

system_prompt = """
# 身份
- 你是一个编程助手，你帮助用户编写Python代码。

# 指令
- 定义变量时，使用snake case命名法，而不是camel case命名法。
- 不要返回markdown格式说明，仅仅返回代码即可。
"""
# 创建智能体
agent = create_agent(
    model = model,
    system_prompt=system_prompt
)
for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="怎样定义string变量记录学校名字，例如`路边一条`")]},
    stream_mode="messages"
):
    print(token.content, end="", flush=True)
    # school_name = "黑马程序员"
