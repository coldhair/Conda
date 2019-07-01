# 数据结构 列表推导式
vec = [2, 4, 6]
a = [3 * x for x in vec]
print(a)
b = [[x, x ** 2] for x in vec]
print(b)
d = [3 * x for x in vec if x > 3]
print(d)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
c = [weapon.strip() for weapon in freshfruit]
print(freshfruit)
print(c)
