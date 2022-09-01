#uuid_share#  ac449bec-1d4b-4358-9c59-78babb1c812d  #
class LogicGate:  # 超类：逻辑门
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

    def performGateLogic():
        pass


class BinaryGate(LogicGate):  # 子类/超类：二元逻辑门
    def __init__(self, name):
        LogicGate.__init__(self, name)  # 调用超类初始化

        self.pinA = None  # 两个引脚A/B
        self.pinB = None  # 引脚的两种可能：接直接输入None，接连接器Connector

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

    def setNextPin(self, source: LogicGate):  # Connector把输出接到某个引脚
        if self.pinA == None:
            self.pinA = source  # source是Connector对象
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class UnitaryGate(LogicGate):
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
    def __init__(self, n):
        UnitaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPinA():
            return 0
        else:
            return 1


class AndGate(BinaryGate):  # 具体的子类
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
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class Connector:
    def __init__(self, fgate, tgate: LogicGate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == '__main__':
    main()
