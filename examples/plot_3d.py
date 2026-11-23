"""رسم ثلاثي الأبعاد — مثال مبسط من استعمالات المحاور في curl3d_ani.py."""

import numpy as np
import matplotlib.pyplot as plt
from arabic_sciplot import arab, arabic_3d_axis_formatter

t = np.linspace(0, 4 * np.pi, 300)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(np.cos(t), np.sin(t), t)
ax.set_title(arab("منحنى حلزوني ثلاثي الأبعاد"))
arabic_3d_axis_formatter(ax)
plt.show()
