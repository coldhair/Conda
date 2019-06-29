# 修改全局变量 num
num = 1


def fun1():
    global num  # 需要使用global关键字
    print(num)
    num = 123
    print(num)


fun1()
print(num)
