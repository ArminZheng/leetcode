from collections import deque


class Queue(deque):
    def isEmpty(self): return len(self) == 0
    enqueue = deque.append
    dequeue = deque.popleft
    size = deque.__len__


class Stack(deque):
    push = deque.append
    def peek(self): return self[-1]
    def isEmpty(self): return len(self) == 0
    size = deque.__len__

    @property
    def weather(self):              # 属性方法
        return self._weather

    @weather.setter
    def weather(self, value):
        print("setting score")
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @staticmethod
    def var_str(date_str):                 # 静态方法：校验输入值类型和大小是否符合咱们的类型。
        year, month, day = tuple(date_str.split("-"))
        if 0 < int(year) and 0 < int(month) <= 12 and 0 < int(day) < 32:
            return True
        else:
            return False

    @classmethod
    def class_method(cls, date_str):      # 类方法

        if cls.var_str(date_str):  # 这里是调用静态方法，注意要用cls.静态方法，原理和实例方法中的self一样，自己可以试试，否则是不能读取的。
            year, month, day = tuple(date_str.split("-"))
            return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    # append pop extend [+ left], index, insert, count("a")
    # remove, reverse, rotate, copy
    dlist=deque([1,'a'])
    dlist.append('b') # 在末尾加数据
    dlist.appendleft(0) # 在最前端插入数据
    print(dlist)
    # 输出 :  deque([0, 1, 'a', 'b'])

    dlist.pop() # 删除末尾的数据
    dlist.popleft() # 删除最前端的数据
    print(dlist)
    # 输出 :  deque([1, 'a'])

    dlist.extend(['b','c']) # 在末尾追加list 数据
    dlist.extendleft([-1,0])# 在前端插入list 数据 (注意反向: 0, -1)
    print(dlist)
    # 输出 : deque([0, -1, 1, 'a', 'b', 'c'])

    print(dlist.index('a')) # 找出 a 的索引位置
    # 输出 :  3

    dlist.insert(2, 555) # 在索引2 的位置插入555
    print(dlist)
    # 输出 :  deque([0, -1, 555, 1, 'a', 'b', 'c'])

    print(dlist.count('a')) # 查找 ‘a’ 的数量
    # output: 1

    dlist.remove(1) # 删除第一个匹配值
    # output: deque([0, -1, 555, 'a', 'b', 'c'])
    dlist.reverse()  # 反向
    print(dlist)
    # 输出 :  deque(['c', 'b', 'a', 555, -1, 0])


    dlist.rotate(-2) # 将左端的元素移动到右端 [rotate: 轮班 旋转 转动] (-2:向下逆时针 或 前移)
    print(dlist)
    # 输出 :  deque(['a', 555, -1, 0, 'c', 'b'])

    dlist.rotate(2) # 将右端的元素移动到左端 (2: 向下顺时针 或 后移 往后撸)
    print(dlist)
    # 输出 :  deque(['c', 'b', 'a', 555, -1, 0])

    dl1=dlist # 赋值 dlist 值变化，dl1的值也会修改 (浅拷贝)
    dl2=dlist.copy() # 拷贝 dlist, 拷贝后对dl修改不影响dlist的值 (深拷贝)
    dlist.pop() # 删除最后一个数据, dl1的值也被修改
    print(dl1) # 输出： deque(['c', 'b', 'a', 555, -1])
    print(dl2) # 输出： deque(['c', 'b', 'a', 555, -1, 0])