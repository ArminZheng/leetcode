from model import model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

# 创建智能体
agent = create_agent(
    model = model,
    system_prompt="像海盗一样说话."
)

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="你是谁？")]},
    stream_mode="messages"
):
    print(token.content, end="", flush=True)

# 提示词优化不是一锤子买卖，而是一个不断优化、测试、再优化的过程。
# 提示词工程（Prompt Engineering）。​
# ​身份（Identity）：描述AI的职责、沟通风格和总体目标。​
# 说明（Instructions）：请指导模型如何生成所需的响应。它应该遵循哪些规则？模型应该做什么，以及模型绝对不能做什么？​
# 示例（Examples）：提供可能的输入示例，以及模型期望的输出。​
# 背景信息（Context）：向模型提供生成响应所需的任何额外信息，例如RAG的额外知识库数据，或您认为特别相关的任何其他数据。
