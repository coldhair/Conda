# 蒙特卡洛求圆周率
from random import random  # 随机函数
from time import perf_counter  # 对程序运行计时

darts = 1000 * 1000  # 足够多的点数目
hits = 0.0  # 目前落在圆内部的点数
start = perf_counter()  # 获取当前系统时间
for i in range(1, darts + 1):
    x, y = random(), random()  # 生成随机坐标
    dist = pow(x ** 2 + y ** 2, 0.5)  # 计算到圆心的距离
    if dist <= 1:  # 比较到圆心的距离是否小于等于1
        hits = hits + 1  # 在圆内部就加1
pi = 4 * (hits / darts)
print('圆周率值是：{}'.format(pi))
print('运行时间是：{:.5f}s'.format(perf_counter() - start))
