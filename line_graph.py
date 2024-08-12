import os

import pandas as pd
import plotly.express as px

x_label = os.environ.get("X_LABEL", "x")
y_label = os.environ.get("Y_LABEL", "y")

df = pd.DataFrame({
    x_label: [float(x) if x.isdigit() else x for x in os.environ.get("X_VALUES", "").split(",")],
    y_label: [float(y) if y.isdigit() else y for y in os.environ.get("Y_VALUES", "").split(",")]
})

fig = px.line(
    df, x=x_label, y=y_label,
    title=os.environ.get("TITLE", "title"),
    markers=True,
)
fig.show()
