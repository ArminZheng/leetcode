from basic.LinearDS.stack import Stack

# linear structure
# 线性结构: 1 栈Stack、2 队列Queue、3 双端队列Dequeue、4 列表List
### 相同: 元素之间只存在先后次序关系
### 不同: 数据项的增减方式有所不同

s = Stack()

print(s.isEmpty())
s.push(4)
Stack.push(s, 5)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
