from langchain.messages import HumanMessage, AIMessage
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from model import model


# 1.指定Model名称，由LangChain自动初始化模型
agent = create_agent(model=model)


if __name__ == "__main__":
    # 阻塞式调用模型，需要传入一个消息列表
    # response = agent.invoke( {"messages": [{"role": "user", "content": "月亮的首都是哪里？"}]})
    # role：消息所属角色，可以是system、user、assistant​
    # content：消息的内容​
    # metadata（可选）：消息的元数据，例如：消息的ID、消耗的token等

    # print(response)
    print("---------------")

    # 流式调用，只需要把调用方式改为stream：
    for token, metadata in agent.stream(
        {"messages": [{"role": "user", "content": "月亮的首都是哪里？"}]},
        stream_mode="messages",
    ):
        if token.content:  # Check if there's actual content
            print(token.content, end="", flush=True)  # Print token

    print("---------------")

    # 调用Agent，发送消息
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content="你好，我是虎哥"),
                AIMessage(content="你好，虎哥，很高兴认识你。"),
                HumanMessage(content="我的名字是什么？"),
            ]
        }
    )

    for message in response['messages']:
        message.pretty_print()
