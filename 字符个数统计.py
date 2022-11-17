# 字符个数统计
# print(len(set(input())))

# 数组排序
# n  = int(input())
# ls = list(map(int, input().split()))
# s = int(input())
# if s:
#     ls.sort(reverse=True)
# else:
#     ls.sort()
# for l in ls:
#     print(l, end=" ")

## 快排, 是一种不稳定的算法, 采用分治的思想
def quickSort(listx):
    if len(listx) <= 1:
        return listx
    pivot = listx[len(listx)//2]  # 取列表中中间的元素为被比较数pivot
    listl = [x for x in listx if x < pivot]  # <pivot的放在一个列表
    listm = [x for x in listx if x == pivot]  # =pivot的放在一个列表
    listr = [x for x in listx if x > pivot]  # >pivot的放在一个列表
    left = quickSort(listl)  # 递归进行该函数
    right = quickSort(listr)  # 递归进行该函数
    return left + listm + right  # 整合


print(quickSort([9, 3, 6, 8, 9, 19, 1, 5]))

s = "hello"
for i in "":
    print("hello")

arr = sorted(list(s))
print(arr)
