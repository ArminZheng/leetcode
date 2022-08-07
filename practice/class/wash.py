# 洗碗工

# Stack 是一个包含 push、peek、isEmpty 和 size 方法的列表。
class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: len(self) == 0
    size = list.__len__

def washWorker(s):
    """
    函数 `washWorker` 将字符串 `s` 作为输入，如果字符串 `s` 是有效的菜号序列，则返回 `True`，否则返回 `False`。
    
    函数 `washWorker` 使用堆栈来跟踪正在清洗的盘子。函数 `washWorker` 还跟踪当前正在清洗的盘子，以及当前正在取出的盘子。
    
    函数 `washWorker` 的工作原理如下：
    
    1. 函数 `washWorker` 从一个空栈开始。
    2. `washWorker` 函数以当前正在清洗的盘子为盘子 0 开始。
    3. 函数 `washWorker` 以当前正在取的盘子为盘子 0 开始。
    4. `washWorker` 功能不断洗碗拿取
    
    :param s: 代表顾客拿菜顺序的一串数字。
    """
    st = Stack()
    # s = input()
    # `now` is the index of the dish that is being washed.
    now = 0 # 正在洗的盘子编号
    i = 0 # 取盘子的次序, s[i] 是取得盘子的编号
    while i < 10 and now < 10:
        k = int(s[i])
        # 洗盘子
        # 如果顾客取到盘子 k, 那么正在洗的盘子 to k 之间的盘子都喜好叠放
        if now <= k:
            for m in range(now, k + 1):
                st.push(m)
                # print("PUSH", m)
            now = k + 1 # 正在洗下一个盘子
        # 取盘子
        # 逐个从顶上取盘子, 从 k 开始取, 一直取到对不上号, 说明要去取得还没洗
        while not st.isEmpty() and st.peek() == int(s[i]):
            m = st.pop()
            # print("POP", m)
            i += 1
    # 能取得都取完了, 如果盘子堆里还有盘子, 说明取得序列不对
    if st.isEmpty():
        print("YES!")
    else:
        print("NO!")
        print

# 1. 洗盘子
# 2. 取盘子
# 3. 如果取得都取完了, 如果盘子堆里还有盘子, 说明取得序列不对
washWorker("1043257689")
