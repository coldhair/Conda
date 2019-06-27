import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi)
plt.plot(x,np.sin(x))
plt.plot(x,np.sin(x-1/4*np.pi))
plt.show() #增加这个代码就可以在SciView中看到图了