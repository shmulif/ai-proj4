import plotly.graph_objects as go
import pandas as pd

# Load CSV and clean up extra columns
df = pd.read_csv("hold_policy.csv", index_col=0)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # Drop bad columns

# Convert axis labels to int
x = df.columns.astype(int)
y = df.index.astype(int)
z = df.values

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

fig.update_layout(
    title='Piglet Strategy 3D Surface',
    scene=dict(
        xaxis_title='Opponent Score (j)',
        yaxis_title='Player Score (i)',
        zaxis_title='Hold Threshold (k)'
    )
)

fig.show()
 
fig.write_image("3d_surface.png", scale=2) 
