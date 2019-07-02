# 元组和序列
t = 12345, 54321, "Hello"
print(t[0])
print(t)
u = t,(1,2,3,4,5)
print(u)
del u[0] # 会报错，元组中的元素不能被删除

