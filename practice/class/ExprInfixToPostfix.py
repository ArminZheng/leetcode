from basic.LinearDS.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    tokenList = split(infixexpr)

    for token in tokenList:
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM" or token in "1234567890":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def split(infixexpr):
    """
    它接受一个字符串并返回字符串中的字符列表

    :param infixexpr: 要转换的中缀表达式。
    :return: 由空格分隔的中缀表达式列表。
    """
    if " " in infixexpr:
        return infixexpr.split()
    else:
        return list(infixexpr)


def toList(infixexpr: str):
    if " " in infixexpr:
        tokenList = infixexpr.split()
    else:
        tokenList = list(infixexpr)
    return tokenList


if __name__ == "__main__":
    print(infixToPostfix("A + B * C + D * E + F"))
    print(infixToPostfix("(A+B)*C"))
    print(infixToPostfix("A+B*C+D*E+F"))

    infixexpr = "(a*b)+(c*d)"
    tokenList = toList(infixexpr)

    print(tokenList)
