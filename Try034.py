# 理解字典的最佳方式是把它看做无序的键=>值对集合。
# 在同一个字典之内，关键字必须是互不相同。
te = {'Jake': 4098, 'Tom': 4011}
te['John'] = 2019
print(te)
print(te['Tom'])
te['Ivy'] = 9012
del te['Jake']
print(te)
print(te.keys())
li = list(te.keys())
print(li)
so = sorted(te.keys())
print(so)

# 字典推导可以用来创建任意键和值的表达式词典
dic = {x: x ** 2 for x in range(1, 5)}
print(dic)

P=dict(Mahao=170,Liming=172,Xiaolv=173,Laodi=165)
print(P) # Python中一定要注意大小写