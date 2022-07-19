from math import sqrt
# n = int(input())
n = 9
for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        print(f"{n} is Not a prime number.")
        break
else:
    print(f"{n} is a prime number.")

# a = [[0]*5]*3
a = [[0 for i in range(5)] for j in range(3)]
print(a)        #[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(len(a))
for obj in a:
    print("11")
    obj.append(3)
print(a)
