# self代表类的实例，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
