import time
class Queue(list):
    """简易版队列

    Args:
        list (list): 继承列表
    """
    isEmpty = lambda self: len(self) == 0
    enqueue = list.append
    dequeue = lambda l: l.pop(0)
    size = list.__len__

def printTask():
    """打印任务
    决策支持问题, 但无法通过规则直接计算

    需要进行模拟打印任务场景, 然后对运行结果进行分析, 以支持对打印机模式设定的「决策」
    """
    


with open("README.md", "r", encoding="UTF-8") as f:
    print("文件类型", type(f))

    print(f"读取4个字节: {f.read(4)}")
    # print(f"读取全部字节: {f.read()}")

    # lines = f.readlines()
    # print(f"readlines type: {type(lines)}")
    time.sleep(0.5)
    for line in f:
        print(f"readlines: {line}")
