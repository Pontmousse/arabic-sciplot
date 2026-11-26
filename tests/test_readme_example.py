from contextlib import chdir
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "basic_2d.py"


class ReadmeExampleTests(unittest.TestCase):
    def test_readme_gain_example_renders_right_to_left(self):
        readme_path = ROOT / "README.md"
        readme = readme_path.read_text(encoding="utf-8")
        snippet = readme.split("```python\n", 1)[1].split("\n```", 1)[0]
        if EXAMPLE.is_file():
            self.assertEqual(snippet + "\n", EXAMPLE.read_text(encoding="utf-8"))

        with TemporaryDirectory() as directory, chdir(directory), plt.rc_context():
            self.addCleanup(plt.close, "all")
            example = {}
            exec(compile(snippet, str(readme_path), "exec"), example)
            path = Path("p-controller-arabic.png")
            self.assertTrue(path.is_file())
            ax = example["ax"]
            self.assertTrue(ax.xaxis_inverted())
            self.assertEqual(ax.yaxis.get_ticks_position(), "right")
            self.assertEqual(ax.get_xticklabels()[0].get_text(), "٠")

            initial_point = ax.collections[0]
            marker = initial_point.get_offset_transform().transform(
                initial_point.get_offsets()
            )[0]
            self.assertAlmostEqual(marker[0], ax.bbox.xmax)
            for curve, steady_level in zip(ax.lines[1:], (8, 6), strict=True):
                points = curve.get_transform().transform(curve.get_xydata())
                np.testing.assert_allclose(points[0], marker)
                self.assertAlmostEqual(points[-1, 0], ax.bbox.xmin)
                self.assertTrue(np.all(np.diff(points[:, 0]) < 0))
                self.assertTrue(np.all(np.diff(points[:, 1]) > 0))
                self.assertAlmostEqual(curve.get_ydata()[-1], steady_level, delta=0.02)
