# Few-Shot examples
# 有的时候我们希望模型按照固定的风格来回答问题，而这种风格又不太好描述，那我们就可以通过举例的方式让模型学习例子来回答。
# 用户只需在输入提示（Prompt）中提供几个输入-输出示例，模型就能理解任务模式并生成符合预期的输出：
from model import model
from langchain.agents import create_agent
from langchain.messages import HumanMessage

system_prompt = """
# 身份
- 你是一个科幻作家，根据用户的要求创建一个太空之都。

# 示例
user：月球的首都是什么？
assistant：月华城（Lunara）—— 镶嵌在月球静海环形山中的水晶穹顶都市，其核心是一座利用月球潮汐能驱动的巨型生态循环塔。

user：火星的首都是什么？
assistant：赤晶城（Aresia）—— 深嵌于火星奥林匹斯山熔岩管内的蜂巢都市，地表仅露出由火星红土烧制而成的螺旋尖塔。
"""

# 创建智能体
agent = create_agent(
    model = model,
    system_prompt=system_prompt
)

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="金星的首都是什么?")]},
    stream_mode="messages"
):
    print(token.content, end="", flush=True)
    # 金晖浮都（Aurora Helioplex）——漂浮于金星约五十二公里高空，由数以千计的蜂巢状六边形平台铰接而成。其外围的“日冕聚能塔”将浓厚的氧化硫云层转化为燃料、建材和纯水；一条名为“熔炉坠锚”的超重型热磁链束斜垂至地表岩浆海，既是都市的位置锚定，也是汲取金星地核熔岩热能的导管。全城依靠环绕自身的旋转环带产生拟重力，而中心“云瞳镜穹”则实时合成金红色晨昏光影，使整座城市仿佛一粒悬浮于金色迷蒙雾气中的活体晶胞。%        
