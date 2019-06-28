# 迭代器与生成器
list=[1,2,3,4]
it=iter(list) # 创建迭代器对象
print(next(it)) # 输出迭代器下一个元素
print(next(it))
print(next(it))

lis=['a','b','c','d']
myit=iter(lis)
for x in myit:
    print(x,end=' ')
