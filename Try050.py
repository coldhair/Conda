# 为输入的整数排序

i = 0
list = []
while True:
    if i < 4:
        num = int(input('输入整数：\n'))
        list.append(num)
        i += 1
    else:
        break
new_list = sorted(list)
for n in new_list:
    print(n)
print(new_list)
