import sys

for line in sys.stdin:
    a, num = 0, line[2:].strip()
    dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for i in range(len(num)):
        if num[i] in dic:
            a += dic[num[i]] * (16 ** (len(num) - i - 1))
        else:
            a += int((num[i])) * (16 ** (len(num) - i - 1))
    print(a)
