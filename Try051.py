# 类对象
class MyClass:
    i=12345
    def f(self):
        return 'Hello world'

# 实例化类
x = MyClass()
print('MyClass类的属性i为：',x.i)
print('MyClass类的方法f输出为：',x.f())
