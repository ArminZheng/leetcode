"""中缀表达式求值
"""
from basic.LinearDS.stack import Stack


def calculet(s) -> float:
    def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        elif op == "-":
            return op1 - op2
        else:  # ^
            return op1 * op2

    def doOperand(token):
        operand2 = operandStack.pop()
        operand1 = operandStack.pop()
        result = doMath(token, operand1, operand2)
        # 单独
        operandStack.push(result)

    def toList(infixexpr: str):
        if " " in infixexpr:
            tokenList = infixexpr.split()
        else:
            tokenList = list(infixexpr)
        return tokenList

    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()  # 操作符号
    operandStack = Stack()  # 操作数
    tokenList = toList(s)
    for token in tokenList:
        if token.isnumeric():
            operandStack.push(float(token))
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                doOperand(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                doOperand(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        topToken = opStack.pop()
        doOperand(topToken)
    return operandStack.pop()

if __name__ == '__main__':
    print(calculet("(5+6)*9"))