# 文件操作
f = open('foo.txt', 'a+')
f.write('我们重新写一次试试？\n是的，吕是好人！\n')
str = f.readline()
print(str)
str = f.readline()
print(str)
f.close()
