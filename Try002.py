from matplotlib import pyplot as plt
import numpy as np
x1 = np.linspace(1, 10, 20)
print(x1)
y1 = x1 * x1 + 2
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
axes.plot(x1, y1, 'r')
plt.show()
'''
如何在独立的浮窗中显示Plot绘图
File->Settings->Tools->Python Scientific
取消掉Show plots in toolwindow选项
'''