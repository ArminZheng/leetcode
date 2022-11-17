import time


f = open("README.md", "w", encoding="UTF-8")
f.write("go go go")
f.close()


"""文件操作
open("path", "mode", encoding="UTF-8")
f.read() 读全部
f.read(4) 读个数 (字符数, 换行符(\n)也是一个字符)
f.readlines() 根据换行符拆分为列表

f.write("writen word")
f.flush() # 之前的写入一次刷入, 就算是 w 模式, 也可以在 flush() 之前多次写入
f.close() # 会自动 flush()
"""
with open("README.md", "r", encoding="UTF-8") as f:
    print("文件类型", type(f))

    print(f"读取4个字节: {f.read(4)}")
    print(f"读取剩余全部字节: {f.read()}")

    lines = f.readlines()
    print(f"readlines type: {type(lines)}")  # <class 'list'>
    time.sleep(0.5)
    for line in f:  # 为可迭代类型
        print(f"readlines: {line}")
