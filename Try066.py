for n in range(2, 1000):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n)


for a in range(10):
    print(f'value of a: {a}')