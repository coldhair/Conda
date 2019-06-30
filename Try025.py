# 数据结构
a = [66.25, 333, 333, 1, 123.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(1))
a.remove(333)  # 删除其中值为333的第一个元素，如果没有，会报错。
print(a)
a.reverse()
print(a)
a.sort()
print(a)

# insert, remove 或 sort 等修改列表的方法没有返回值。
