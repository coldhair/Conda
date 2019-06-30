# 将列表当队列使用
from collections import deque

queue = deque(['Eric', 'Tom', 'John'])
queue.append('coldhair')
queue.append('Yanpeng')
print(queue)
a = queue.popleft()
print(a)
a = queue.popleft()
print(a)
print(queue)
