from basic.stack import Stack

def divideBy2(decNumber, factor=16):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % factor
        remstack.push(rem)
        decNumber = decNumber // factor

    binString = ""
    while not remstack.isEmpty():
        binString += digits[remstack.pop()]
    return binString


if __name__ == "__main__":
    print(divideBy2(233))

# Deprecated
def charNumber(num):
    if num > 9:
        return chr(ord('A') + num - 10)
    return str(num)
