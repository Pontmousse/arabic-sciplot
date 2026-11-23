import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import arabic_sciplot as arabic  # استيراد الحزمة المنشورة بدل الملف المحلي

def vector_field_with_curl(x, y):
    u = -y
    v = x
    return u, v

# def vector_field_with_curl(x, y):
#     u = -y * np.sin(x)
#     v = x * np.cos(y)
#     return u, v

def compute_curl(x, y, u, v):
    dy, dx = x[1, 0] - x[0, 0], y[0, 1] - y[0, 0]  # Grid spacing
    dv_dx = np.gradient(v, dx, axis=1)
    du_dy = np.gradient(u, dy, axis=0)
    curl = dv_dx - du_dy
    return curl

def plot_static_curl_field_2d():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(arabic.arab("تمثيل ثنائي الأبعاد للدوران في مجال شعاعي"))  # ✅ Arabic title
    arabic.arabic_2d_axis_formatter(ax)

    plt.tight_layout()

    # Grid
    X, Y = np.meshgrid(
        np.linspace(-4, 4, 20),
        np.linspace(-4, 4, 20)
    )

    u, v = vector_field_with_curl(X, Y)
    curl = compute_curl(X, Y, u, v)

    # Plot curl as background colormap
    # c = ax.pcolormesh(X, Y, curl, shading='auto', cmap=cm.RdBu)
    # cbar = plt.colorbar(c, ax=ax, shrink=0.8)
    # cbar.set_label(arabic.arab("الدوران"))  # ✅ Arabic label for curl

    # Overlay vector field
    ax.quiver(X, Y, u, v, angles='xy', scale_units='xy', scale=20, color='black')

    plt.show()

if __name__ == "__main__":
    plot_static_curl_field_2d()
