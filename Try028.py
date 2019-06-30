# for循环的嵌套

f = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            for g in range(1, 5):
                a = i * 1000 + j * 100 + k * 10 + g
                f += 1
                print(a, '-', f)

print(4 ** 4)
