import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter
import numpy as np

from arabic_sciplot import arabic_2d_axis_formatter


target = 10.0  # cm
initial_level = 2.0  # cm
leak_rate = 1.0  # cm/s, equivalent rate of fall with the tap shut
time = np.linspace(0.0, 26.0, 521)

navy = "#192e47"
muted = "#4d6074"
teal = "#087c78"
rust = "#ac5023"
font_family = ["DejaVu Sans"]
if "Noto Sans Arabic" in font_manager.get_font_names():
    font_family.insert(0, "Noto Sans Arabic")
plt.rcParams.update({
    "font.family": font_family,
    "text.color": navy,
    "axes.labelcolor": navy,
    "xtick.color": muted,
    "ytick.color": muted,
})

fig, ax = plt.subplots(figsize=(8.2, 5.35), facecolor="white")
fig.subplots_adjust(left=0.075, right=0.87, bottom=0.233, top=0.765)

ax.set(xlim=(0, 26), ylim=(0, 11.1))
ax.set_xticks(np.arange(0, 25, 4))
ax.set_yticks(np.arange(0, 11, 2))
arabic_2d_axis_formatter(
    ax, invert_x=True, y_on_right=True,
    tick_direction="out", tick_length=4, tick_labelsize=11,
)
arabic_digits = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
for axis in (ax.xaxis, ax.yaxis):
    axis.set_major_formatter(
        FuncFormatter(lambda value, _: f"{value:.0f}".translate(arabic_digits))
    )
ax.set_xlabel("الزمن (ثانية)", fontsize=13)
ax.xaxis.set_label_coords(0.5, -0.165)
ax.set_ylabel("مستوى الماء (سم)", fontsize=13, labelpad=12)

ax.set_axisbelow(True)
ax.grid(axis="y", color="#e3e9ee", linewidth=0.8)
ax.spines[["top", "left"]].set_visible(False)
ax.spines[["right", "bottom"]].set_color("#b6c3cf")
ax.axhline(target, color="#65768a", linestyle=(0, (5, 4)), linewidth=1.35, zorder=2)
ax.text(0.55, 10.14, "المستوى المطلوب",
        ha="right", va="bottom", color=muted, fontsize=12)
ax.text(21.1, 10.14, "خطأ الاستقرار",
        ha="center", va="bottom", color=muted, fontsize=12)

for gain, gain_label, color, arrow_x, label_y, error_label in (
    (0.50, "الكسب ٠٫٥ لكل ثانية", teal, 19.5, 9.0, "٢ سم"),
    (0.25, "الكسب ٠٫٢٥ لكل ثانية", rust, 22.8, 7.15, "٤ سم"),
):
    equilibrium = target - leak_rate / gain
    level = equilibrium + (initial_level - equilibrium) * np.exp(-gain * time)

    ax.plot(time, level, color=color, linewidth=2.8, zorder=3)
    label_x = 12.3
    curve_y = np.interp(label_x, time, level)
    ax.text(label_x, curve_y + 0.24, gain_label,
            color=color, fontsize=13, va="bottom", ha="center")

    arrow_level = float(np.interp(arrow_x, time, level))
    ax.annotate("", xy=(arrow_x, arrow_level), xytext=(arrow_x, target),
                arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.3,
                            "shrinkA": 2, "shrinkB": 3})
    ax.text(arrow_x + 0.3, label_y, error_label,
            ha="right", va="center", color=color, fontsize=11.5)

ax.scatter([0], [initial_level], color=navy, s=17, zorder=4, clip_on=False)
fig.text(0.922, 0.915, "التحكّم التناسبي في مستوى الماء",
         ha="right", va="center", fontsize=24, fontweight="bold")
fig.text(0.922, 0.845, "استجابة دلو يتسرّب منه الماء عند قيمتين للكسب التناسبي",
         ha="right", va="center", fontsize=13, color=muted)
fig.text(0.922, 0.058,
         "نموذج مبسّط يبدأ من ٢ سم، مع تسرّب ثابت يعادل انخفاضًا قدره ١ سم في الثانية.",
         ha="right", va="center", fontsize=10.5, color=muted)

fig.savefig("p-controller-arabic.png", dpi=300)
