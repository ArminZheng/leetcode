class DecoratorPerson:
    """装饰器方式"""

    def __init__(self) -> None:
        self.__age = 0

    @property  # @property 表示把方法当作属性使用, 表示获取属性时会执行下面修饰的方法
    def age(self):  # 装饰器方式的 property 属性修饰的方法名一定要一样
        return self.__age

    @age.setter  # 方法名.setter 表示把方法当作属性使用, 表示设置属性时会执行下面修饰的方法
    def age1(self, age):  # 方法名要一样: 因为赋值操作会自动调用该方法
        """
        def age1(self, value) 代表: p.age1 = 1 
        @age.setter 代表 @property def age(self)
        """
        if age >= 150:
            print("???")
        else:
            self.__age = age


class ClassPerson:
    """类属性方式"""

    def __init__(self) -> None:
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 150:
            print("???")
        else:
            self.__age = age

    age = property(get_age, set_age)  # 先: 获取方法签名, 后: 设置方法签名


# opt + click = 同级折叠
if __name__ == '__main__':
    p = DecoratorPerson()
    p1 = DecoratorPerson()
    p.age1 = 150
    p1.age1 = 150
    print(p.age)
    print(p1.age)
    p.age1 = 149
    p1.age1 = 149
    print(p.age)
    print(p1.age)


def generator(num):
    for i in num:
        print("start")
        yield i
        print("generate completion")


def testGenrator(generator):
    g = generator(range(100))
    print(next(g))
    print(next(g))
    for i in g:
        print(i)

# testGenrator(generator)


def fb(num):
    a, b = 0, 1
    # 记录生成了几个数字
    index = 0
    while index < num:
        result = a
        a, b = b, a + b
        yield result  # yield
        index += 1


def testFb():
    f = fb(5)
    for i in f:
        print(i)
