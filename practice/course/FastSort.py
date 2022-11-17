# https://blog.csdn.net/weixin_59512744/article/details/119935018


def quickAscSort(arr, left, right):  # 升序 ascending
    if left >= right:
        return arr
    init_left = left
    init_right = right
    key = arr[left]
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[left] = key
    quickAscSort(arr, init_left, left-1)
    quickAscSort(arr, left+1, init_right)
    return arr


def quickDescSort(arr, left, right):  # 降序 descending
    if left >= right:
        return arr

    init_left = left
    init_right = right
    key = arr[right]

    while left < right:
        while left < right and arr[left] >= key:
            left += 1
        arr[right] = arr[left]
        while left < right and arr[right] <= key:
            right -= 1
        arr[left] = arr[right]
    arr[right] = key
    quickDescSort(arr, init_left, left-1)
    quickDescSort(arr, right+1, init_right)
    return arr


def quickSort(listx):
    if len(listx) <= 1:
        return listx
    pivot = listx[len(listx) // 2]  # 取列表中中间的元素为被比较数pivot
    listl = [x for x in listx if x < pivot]  # <pivot的放在一个列表
    listm = [x for x in listx if x == pivot]  # =pivot的放在一个列表
    listr = [x for x in listx if x > pivot]  # >pivot的放在一个列表
    left = quickSort(listl)  # 递归进行该函数
    right = quickSort(listr)  # 递归进行该函数
    return left + listm + right  # 整合


def quickAntiSort(listx):
    if len(listx) <= 1:  # fast-fail
        return listx
    pivot = listx[len(listx) // 2]  # 取列表中中间的元素为被比较数pivot
    listl = [x for x in listx if x < pivot]  # <pivot的放在一个列表
    listm = [x for x in listx if x == pivot]  # =pivot的放在一个列表
    listr = [x for x in listx if x > pivot]  # >pivot的放在一个列表
    left = quickAntiSort(listl)  # 递归进行该函数
    right = quickAntiSort(listr)  # 递归进行该函数
    return right + listm + left  # 整合 = 大 中 小 (递归底层是)


print(quickSort([9, 3, 6, 8, 9, 19, 1, 5]))
print(quickAntiSort([9, 3, 6, 8, 9, 19, 1, 5]))
print(quickDescSort([9, 3, 6, 8, 9, 19, 1, 5], 0, 7))
print(quickAscSort([9, 3, 6, 8, 9, 19, 1, 5], 0, 7))


def quickSorted(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    l_little = [x for x in l if x < pivot]
    l_equal = [x for x in l if x == pivot]
    l_bigger = [x for x in l if x > pivot]
    little = quickSorted(l_little)
    bigger = quickSorted(l_bigger)
    return little + l_equal + bigger

# 分而治之的思想
print("hello? ", quickSorted([9, 3, 6, 8, 9, 19, 1, 5]))
print(max([1]*0))
