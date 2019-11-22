import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
mpl.use('macosx')
plt.style.use('dark_background')
# plt.grid()
# plt.draw()
# plt.show()
x = np.linspace(-1, 1, 1000)
def fun(n):
    # x = np.linspace(-1, 1, 1000)
    y = x**n

# plt.grid('on') :
# plt.ylim(0, 2)
# plt.xlim(0, 2)
#plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(8, 6))
ax.plot(x,fun(n))
for i in ax:
    for j in i:
        # print(j)
        j.plot(x, y)
        j.grid(ls='--', lw=0.5, c='gray')
        j.set_ylim(-1, 1)
        j.set_xlim(-1, 1)
        j.spines['left'].set_position('center')
        j.spines['right'].set_color('none')
        j.spines['bottom'].set_position('center')
        j.spines['top'].set_color('none')
        # j.spines['left'].set_smart_bounds(True)
        # j.spines['bottom'].set_smart_bounds(True)
        # j.xaxis.set_ticks_position('bottom')
        # j.yaxis.set_ticks_position('left')
# ax[i,j].plot(x, y)
# ax[i,j].grid(ls='--', lw=0.5, c='gray')
# ax[i,j].set_ylim(0, 2)
# ax[i,j].set_xlim(0, 2)

