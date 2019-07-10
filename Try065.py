d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
print(d.values())
# print(d.itervalues()), python3中只有d.values( )方法了，迭代的没有了
print(enumerate(d))
for k in enumerate(d):
    print(k)
    print(k[1])

for v in d.values():
    print(v)
