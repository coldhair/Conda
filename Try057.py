add = lambda x, y: x + y
a = add(3, 5)
print(a)


# 以列表的第二个元素进行排序
def take_second(elem):
    return elem[1]


rand = [(2, 2), (3, 4), (4, 1), (1, 3)]

rand.sort(key=take_second)
print(rand)
