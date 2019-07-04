"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 吕艳朋
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{1}×{0}={2}'.format(i, j, i * j), end=' ')
    print()
