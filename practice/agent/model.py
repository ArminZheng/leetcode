from typing import cast
# 或者从 langchain_core 导入，取决于你的版本
from langchain_core.language_models import BaseChatModel
# 导入Langchain的初始化模型的函数
from langchain.chat_models import init_chat_model
# 非支持模型无法自动加载环境遍历，我们需要自己加载环境变量中的base_url和api_key
import os
# 加载环境变量
from dotenv import load_dotenv
load_dotenv()



base_url = os.getenv("SENSENOVA_BASE_URL")
api_key = os.getenv("SENSENOVA_API_KEY")
model_name = os.getenv("SENSENOVA_MODEL")

# 调用init_chat_model函数初始化模型，参数model用来指定模型名称，Langchain会根据模型名字自动设定base_url，并从环境变量中获取api_key
# model = init_chat_model(model="deepseek-chat")
# 初始化模型

model = cast(BaseChatModel, init_chat_model(
    model=model_name, # 模型名称，这里可以自定义，我们用的是阿里的qwen-max
    model_provider="openai", # 如果是Langchain不支持的模型，需要指定模型提供者（虽然我们用的是阿里，但是阿里兼容openai，所以这里用openai，就是默认采用openai的API规范）
    base_url=base_url,
    api_key=api_key,
    # temperature: 控制生成文本的随机性，值越小越确定，值越大越随机
    temperature=1.5,
))

if __name__ == "__main__":
    print(type(model)) # <class 'langchain_openai.chat_models.base.ChatOpenAI'>

    # 调用invoke方法
    response = model.invoke("月亮的首都是哪里？")

    # 查看响应结果
    print(response)

    # 通过.stream方法实现流式访问
    stream = model.stream("月亮的首都是哪里？")

    # stream调用返回的结果是一个generator，方便我们循环获取结果
    print(type(stream))

    # 遍历stream结果，实时打印AI的回复
    for chunk in stream:
        print(chunk.content, end="", flush=True)
