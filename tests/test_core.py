import unittest

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from arabic_sciplot import (
    arab, custom_formatter, custom_log_formatter, generate_tickvals_and_text,
    arabic_2d_axis_formatter, arabic_3d_axis_formatter,
)


class CoreTests(unittest.TestCase):
    def test_native_text_and_formatters(self):
        self.assertEqual(arab("مرحبًا"), "مرحبًا")
        self.assertEqual(custom_formatter(-2), "2.00-")
        self.assertEqual(custom_formatter(-2, 0), "2.00-")
        self.assertEqual(custom_log_formatter(0), "0")
        self.assertEqual(custom_log_formatter(10, 0), "$^{1}10$")

    def test_tick_generation(self):
        positions, labels = generate_tickvals_and_text([0, 1], num_ticks=3)
        self.assertEqual(positions, [0, 0.5, 1])
        self.assertEqual(labels, ["0.00", "0.50", "1.00"])

    def test_configurable_axes(self):
        fig, ax = plt.subplots()
        arabic_2d_axis_formatter(ax)
        self.assertTrue(ax.xaxis_inverted())
        self.assertEqual(ax.yaxis.get_ticks_position(), "right")
        arabic_2d_axis_formatter(ax, invert_x=False, y_on_right=False,
                                 tick_direction="out", tick_length=4)
        self.assertFalse(ax.xaxis_inverted())
        self.assertEqual(ax.yaxis.get_ticks_position(), "left")
        plt.close(fig)
        fig = plt.figure()
        ax3 = fig.add_subplot(111, projection="3d")
        arabic_3d_axis_formatter(ax3)
        self.assertTrue(ax3.xaxis_inverted())
        self.assertTrue(ax3.yaxis_inverted())
        plt.close(fig)


if __name__ == "__main__":
    unittest.main()
