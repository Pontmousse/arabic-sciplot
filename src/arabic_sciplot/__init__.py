"""أدوات تنسيق الرسوم العلمية بالعربية."""

from .text import arab
from .ticks import (
    custom_formatter,
    custom_log_formatter,
    generate_tickvals_and_text,
    pi_formatter,
)
from .matplotlib import (
    arabic_2d_axis_formatter,
    arabic_3d_axis_formatter,
    arabic_3d_plot_formatter,
)

__all__ = [
    "arab", "custom_formatter", "custom_log_formatter", "pi_formatter",
    "generate_tickvals_and_text", "arabic_2d_axis_formatter",
    "arabic_3d_axis_formatter", "arabic_3d_plot_formatter",
]
