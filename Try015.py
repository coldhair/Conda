# 函数学习

def ChangInt(a):
    a = 10


b = 2
c = ChangInt(b)
print(c)
print(b)
print(a) #变量a在函数内部，这么用会报错‘NameError: name 'a' is not defined’