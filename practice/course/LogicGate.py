#uuid_share#  ac449bec-1d4b-4358-9c59-78babb1c812d  #
class LogicGate:
    """超类：逻辑门
    """

    def __init__(self, name):  # 初始化属性：名称
        self.label = name
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        if self.output is None:
            self.output = self.performGateLogic()  # 运算：超类中无法定义
        return self.output

    def setNextPin(self, source):
        pass

    def performGateLogic(self):
        pass


class Connector:
    """连接器
    输入-输出
    """

    def __init__(self, fgate: LogicGate, tgate: LogicGate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class BinaryGate(LogicGate):
    """子类/超类：二元逻辑门
    """

    def __init__(self, name):
        LogicGate.__init__(self, name)  # 调用超类初始化

        self.pinA: Connector = None  # 两个引脚A/B
        self.pinB: Connector = None  # 引脚的两种可能：接直接输入None，接连接器Connector

    def getPinA(self):  # 取A引脚的值，按照两种可能取值
        if self.pinA == None:
            return int(
                input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            # pinA接Connector，其值来源于fromgate的输出
            return self.pinA.getFrom().getOutput()

    def getPinB(self):  # 取B引脚的值，按照两种可能取值
        if self.pinB == None:
            return int(
                input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source: Connector):  # Connector把输出接到某个引脚
        if self.pinA == None:
            self.pinA = source  # source是Connector对象
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class UnitaryGate(LogicGate):
    """子类/超类：一元逻辑门
    """

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None

    def getPinA(self):
        if self.pinA == None:
            return int(
                input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            # pinA接Connector，其值来源于fromgate的输出
            return self.pinA.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnitaryGate):
    """具体的子类: 非门
    """

    def __init__(self, n):
        UnitaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPinA():
            return 0
        else:
            return 1


class AndGate(BinaryGate):
    """具体的子类: 与门
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):  # 终于实现了逻辑运算
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """具体的子类: 或门
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class XORGate(BinaryGate):
    """具体的子类: 异或门

    半加器 (无低位的进位输入, 有高位的进位输出. 异或+与实现)
    全加器 (全进位功能, 加法器)
        1位全加器 One full adder (二进制加法电路)
        4位全加器 (多位全加器连接可以 逐位进位 (也称串行进位), 也可以 超前进位)

        Carry in
         ⬇
    A -> [] 
         [] -> Sum
    B -> []
         ⬇
        Carry out

    (三个输入两个输出)


    半加器实现: 1个 异或 + 1个 与 (异或可以得到和, 与可以得到进位)
    
    全加器: 在半加器的基础上, 使能够处理低位过来的进位, 记住最多只有三个1输入, 所以最多只输出 11 (2进制)
    全加器实现: 
        在半加器的基础上再添加一个半加器的结构, 低位的进位 与 Sum 进行 (XOR 和 AND)
        这两个半加器的 AND 都会产生 Carry out, 因此将所有进位进行 OR  (4个数至少有 2个 1 就能进位) 最终构成了全加器
        实现统计: 
            2 XOR + 2 AND + 1 OR
            2 XOR + 3 AND + 1 OR
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1 and b == 0) or (a == 0 and b == 1):
            return 1
        else:
            return 0


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    # c1 = Connector(AndGate("G1"), OrGate("G3"))
    # c2 = Connector(AndGate("G2"), OrGate("G3"))
    # c3 = Connector(OrGate("G3"), NotGate("G4"))
    print(g4.getOutput())


if __name__ == '__main__':
    main()
