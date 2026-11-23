# Re-import after reset and regenerate the animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from scipy.interpolate import BSpline
from arabic_sciplot import arab, arabic_2d_axis_formatter

# Degree and control points
degree = 2
control_points = np.array([
    [0, 0],
    [1, 2],
    # [3, 3],
    # [4, 0],
    [5, -1],
    # [7, 2],
    [8, 0]
])
n = len(control_points) - 1

# # Uniform, clamped knot vector
knots = np.concatenate(([0] * (degree + 1),
                        np.arange(1, n - degree + 1),
                        [n - degree + 1] * (degree + 1)))

print(knots)
# Fully uniform, non-clamped:
# knots = np.arange(0, n + degree + 2)


# Parameter range
t_min = knots[degree]
t_max = knots[-degree-1]
t_vals = np.linspace(t_min, t_max, 200)

# Create B-spline curve
spline = BSpline(knots, control_points, degree)
curve = spline(t_vals)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(control_points[:, 0], control_points[:, 1], 'o--', label=arab('مضلّع التحكّم'))
ax.plot(curve[:, 0], curve[:, 1], label=arab('المنحنى المبني على العقد'), alpha=0.5)
point_plot, = ax.plot([], [], 'ro', label=arab('النقطة الحالية'))
weights_plot, = ax.plot([], [], 'go', label=arab('تأثير نقاط التحكّم'))
ax.legend()
# ax.set_title("B-spline Curve and Basis Function Influence Animation")
ax.grid()
ax.axis('equal')

arabic_2d_axis_formatter(ax)

# Animation function
def animate(i):
    print(f"Animating frame {i+1}/{len(t_vals)}")
    t = t_vals[i]
    C_t = spline(t)
    
    # Compute basis functions at t
    weights = np.zeros(n + 1)
    for j in range(n + 1):
        coeff = np.zeros(n + 1)
        coeff[j] = 1
        basis_func = BSpline(knots, coeff, degree)
        weights[j] = basis_func(t)
    
    # Active control points weighted by basis functions
    active_pts = control_points * weights[:, np.newaxis]
    
    # Update plots
    point_plot.set_data(C_t[0], C_t[1])
    weights_plot.set_data(active_pts[:, 0], active_pts[:, 1])
    return point_plot, weights_plot

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(t_vals), interval=50, blit=True)
plt.close(fig)

# Save as GIF
writer = PillowWriter(fps=30)
name = 'bspline_curve_deg0.gif'
ani.save(name, writer=writer, dpi=300)
print(f"B-spline animation saved as {name}.\n\n")
