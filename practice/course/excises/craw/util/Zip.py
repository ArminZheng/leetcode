a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 4, 5, 6]

# zip([iterable, ...])

print(zip(a, c))  # <zip object at 0x1006ce880>
print(list(zip(a, c)))  # [(1, 7), (2, 8), (3, 9)]

# 利用 * 号操作符, 将元组解压为列表
# 如果迭代对象里面是元祖, 就会分解; 如果不是就会压缩
print(zip(*zip(a, c)))  # <zip object at 0x1006ce9c0>

print(zip(*zip(a, c)))
print(type(zip(*zip(a, c))))
a1, a2 = zip(*zip(a, c))

print(a1)  # (1, 2, 3)
print(a2)  # (7, 8, 9)
