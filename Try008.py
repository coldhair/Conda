# 猜数字游戏
import random
n=random.randrange(1,10)
# print(n)
g= -1
print('猜数字游戏！')
while g != n:
    g=int(input("请输入你猜的数字："))

    if g==n:
        print("恭喜，你猜对了，迷底就是",n)
    elif g<n:
        print('你猜的数字小了')
    elif g>n:
        print('你猜的数字大了')