# 递归函数
# 计算阶乘 n! = 1 * 2 * 3 * ... * n

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


s = fact(4)
print(s)
