from queue import Queue


"""queue.Queue 可用于多线程之间的、线程安全的队列
"""
# 创建Queue
q = Queue()

# 添加元素, 满时会「阻塞」
q.put(item="hello")

# 获取元素, 为空时会「阻塞」
item = q.get()

# 状态
q.qsize()  # 查看元素多少
q.empty()
q.full()  # 是否已满
