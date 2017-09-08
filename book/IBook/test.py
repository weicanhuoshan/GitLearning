import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimg



x = np.linspace(-10,10,51)
y = np.arctan(x)

fig, axes = plt.subplots(nrows=1, ncols=2)
ax0, ax1 = axes.flatten()
ax0.set_title('ori')
ax0.plot(x, (y>0)*2-1)
ax0.plot(x, x==0)
ax0.plot(x, x*0+0.5, '--')
ax0.grid()
ax1.set_title('gradient')
ax1.plot(x, y)
ax1.plot(x, 1/(x**2+1))
ax1.plot(x, x*0+0.5, '--')
ax1.grid()
fig.tight_layout()
plt.show()