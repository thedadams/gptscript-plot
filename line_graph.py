import os

import pandas as pd
import plotly.express as px

x_label = os.environ.get("x-label", "x")
y_label = os.environ.get("y-label", "y")

df = pd.DataFrame({
    x_label: [float(x) if x.isdigit() else x for x in os.environ.get("x-values", "").split(",")],
    y_label: [float(y) if y.isdigit() else y for y in os.environ.get("y-values", "").split(",")]
})

fig = px.line(
    df, x=x_label, y=y_label,
    title=os.environ.get("title", "title"),
    markers=True,
)
fig.show()
