# 将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

while stack != []:
    a = stack.pop()
    print(a)
