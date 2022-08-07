from basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = split(postfixExpr)

    formula = ""

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            # 单独
            formula += (str(operand1) + token + str(operand2) + " ")
            operandStack.push(result)
    return operandStack.pop(), formula

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def split(infixexpr):
    if " " in infixexpr:
        return infixexpr.split()
    else:
        return list(infixexpr)

# ABC*+DE*+F+
# AB+C*
# ABC*+DE*+F+
reslut, formula = postfixEval("996*+92*+4+")
print(formula, "= ", reslut, sep="")
print(postfixEval("996*+92*+4+"), sep="")
print(postfixEval("23*4+")[0], sep="")