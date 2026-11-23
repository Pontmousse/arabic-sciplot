"""تدريجات Plotly — مستلهمة من app_parametric_mvf.py."""

import numpy as np
import plotly.graph_objects as go
from arabic_sciplot import generate_tickvals_and_text

x = np.linspace(-np.pi, np.pi, 100)
tickvals, ticktext = generate_tickvals_and_text(
    x, num_ticks=5, use_pi_format=True
)
fig = go.Figure()
fig.add_scatter(x=x, y=np.sin(x))
fig.update_xaxes(title="س", tickvals=tickvals, ticktext=ticktext)
fig.show()
