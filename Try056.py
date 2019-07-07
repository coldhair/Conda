# 类的继承
# class definition
class people:
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weithgt = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weithgt = w

    def speak(self):
        print('{}说：我{}岁。'.format(self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print('{}说：我{}岁了，在读{}年级。'.format(self.name, self.age, self.grade))


# 另一个类
class spearker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print('我叫{}，我是一个演说家，我演讲的主题是{}'.format(self.name, self.topic))


# 多重继承

class sample1(student, spearker):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        spearker.__init__(self, n, t)


test1 = sample1('Tim', 25, 80, 4, 'Python')
test1.speak()


class sample2(spearker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        spearker.__init__(self, n, t)


test2 = sample2('Tim', 25, 80, 4, 'Python')
test2.speak()
