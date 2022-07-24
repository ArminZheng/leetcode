from basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    if " " in infixexpr:
        tokenList = infixexpr.split()
    else:
        tokenList = list(infixexpr)

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

if __name__ == "__main__":
    print(infixToPostfix("A + B * C + D * E + F"))
    print(infixToPostfix("(A+B)*C"))
    print(infixToPostfix("A+B*C+D*E+F"))

    infixexpr = "(a*b)+(c*d)"
    if " " in infixexpr:
        tokenList = infixexpr.split()
    else:
        tokenList = list(infixexpr)

    print(tokenList)