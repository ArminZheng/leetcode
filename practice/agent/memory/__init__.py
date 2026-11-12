# 对于智能体而言，记忆分为了两类：
# - 短期记忆（short-term memory）
# - 长期记忆（long-term memory)

# 注意，大家不要被字面上的意思误导了，很多人看到名字就误以为：短期记忆就是临时记忆，断电就没了；长期记忆就是永久记忆，持久保存。

# 更准确的替代叫法其实是有的：工作记忆/会话记忆 vs 持久记忆。有些工程文章已经改用“Working Memory”和“Persistent Memory”来避免歧义。但“短期/长期”因为心理学渊源和社区惯性，已经成了事实上的默认术语，改起来成本高，所以教程只能一边用一边解释。

# 简单用一句话概括的话：
# - 短期记忆：当前任务或会话的上下文（Working Memory 或 Session Memory）
# - 长期记忆：跨任务或会话的经验与知识（Persistent Memory）

# 由于短期记忆通常生命周期是当前会话，所以我们也可以称为会话记忆。
# Agent的会话记忆通常包含三部分：
# - 对话历史
# - 查询结果
# - 任务状态

"""
AgentState + Checkpointer

LangChain提供了自动化的记忆管理方案：
- 首先，LangChain把会话记忆（也就是Messages列表）记录为AgentState的一部分
- AgentState通过Checkpointer对象来保存，每一次与AI的交互都会生成一个快照，记录为一个StateSnapshot，把同一会话的所有StateSnapshot组合在一起，就是完整的会话历史了。
- 为了区分不同的会话记忆，不同会话需要设定各自的thread_id，相同会话则使用相同thread_id
- 向Agent发起会话时必须指定自己的thread_id以唤起对应的会话记忆

目前我们使用的checkpointer是基于内存的InMemorySaver，LangChain也提供了很多持久化存储的checkpointer，例如：
- SqlLiteSaver ：基于sqlite存储
- PostgresSaver ：基于Postgres存储
- CosmosDBSaver ：使用Azure Cosmos DB的实现

具体可以查看文档：
https://docs.langchain.com/oss/python/langgraph/persistence#checkpointer-libraries
"""

"""
6.3 记忆管理策略
由于会话记忆要保存会话的历史，并且在调用LLM时携带历史消息列表。而当会话越来越长时，历史消息就可能超过LLM的上下文限制。例如，DeepSeek的上下文不能超过128K.
"""
