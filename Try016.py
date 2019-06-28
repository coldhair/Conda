# 传可变对象实例
def changeme(lis):
    lis.append([1, 2, 3, 4])
    print('函数内取值：', lis)
    return lis


mylist = [10, 20, 30]
see = changeme(mylist)
print('函数外取值：', see)
print('函数外取值：', mylist)


def printme(str):
    # 打印任何传入的字符串
    print(str)
    return


# 调用printme函数
printme(str='菜鸟教程')

# 默认参数的函数
def dayinInfo(name,age=36):
    print('名字：',name)
    print('年龄：',age)
    return
#调用dayinInfo函数
dayinInfo(age=50,name='吕艳朋')
print('---------------')
dayinInfo(name='吕艳风')
