# 传可变对象实例
def changeme(lis):
    lis.append([1, 2, 3, 4])
    print('函数内取值：', lis)
    return lis


mylist = [10, 20, 30]
see = changeme(mylist)
print('函数外取值：', see)
print('函数外取值：', mylist)
