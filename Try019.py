# 字典形式传入的参数
def pdinfo(arg1, **vardict):
    print('输出：')
    print(arg1)
    print(vardict)


# 调用pdinfo函数
pdinfo(1, a=2, b=3)


# 如果单独出现星号 * 后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c


d = f(1, 2, c=3)
print(d)

sum = lambda var1, var2: var1 + var2
print(sum(10, 20))
print(sum(20, 20))
