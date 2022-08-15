import math


def func1():
    print("func1 start exec")
    num = 1 / 0
    print("func1 ended")


def func2():
    print("func2 start exec")
    func1()
    print("func2 ended exec")


def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了, 异常信息是: {e}")


if __name__ == "__main__":
    main()

print("step 0")
print(__name__)

def min() -> int:
    min_ = [math.inf]
    return min_[-1]

print(min())
