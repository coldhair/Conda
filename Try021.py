# 全局变量和局部变量
total = 0


def sum(var1, var2):
    total = var1 + var2
    print("函数内是局部变量：", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量：", total)
