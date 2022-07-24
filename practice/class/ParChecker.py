from basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                break
            else:
                to = s.pop()
                b = match(symbol, to)
                if not b:
                    break
        index += 1
    else:
        if not s.isEmpty():
            balanced = False
            print("aha")
    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(a, b):
    if a == b:
        return True
    return False

if __name__ == '__main__':
    print(parChecker("((()])"))
    print("======")
    print(parChecker("(([]))"))