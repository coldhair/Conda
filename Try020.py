# return语句
def sum1(arg1, arg2):
    total1=arg1+arg2
    print('函数内：',total1)
    return total1

# 调用sum函数
total1= sum1(20, 30)
print('函数外：',total1)


# return语句
def sum2(arg1, arg2):
    total2=arg1+arg2
    print('函数内：',total2)
    return None

# 调用sum函数
total2= sum2(20, 30)
print('函数外：',total2)