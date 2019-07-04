# 输出
print('{0}和{1}'.format('Google','Baidu'))
print('{1}和{0}'.format('Google','Baidu'))

for x in range(1,11):
    print('{0:2d}{1:4d}{2:5d}'.format(x,x*x,x*x*x))

import math
print(math.pi)
print('{!r}'.format(math.pi))
print('{0:.3f}'.format(math.pi))
