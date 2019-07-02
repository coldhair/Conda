# 集合也支持推导式

a = {x for x in 'abcdefg' if x not in 'abc'}
print(a)  # 最后出现的结果顺序很有意思，怎么回事？
