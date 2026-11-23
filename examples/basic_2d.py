"""رسم علمي ثنائي الأبعاد — مثال مختصر مستلهم من رسوم الموسوعة العربية."""

import numpy as np
import matplotlib.pyplot as plt
from arabic_sciplot import arab, arabic_2d_axis_formatter

x = np.linspace(-5, 5, 200)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(arab("تمثيل دالة تربيعية"))
arabic_2d_axis_formatter(ax)
plt.show()
