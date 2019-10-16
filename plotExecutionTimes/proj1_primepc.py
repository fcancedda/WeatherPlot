import plotly.graph_objects as go
import pandas as pd
import numpy as np

rs = np.random.RandomState()
rs.seed(0)

# def brownian_motion(T = 1, N = 100, mu = 0.1, sigma = 0.01, S0 = 20):
#     dt = float(T)/N
#     t = np.linspace(0, T, N)
#     W = rs.standard_normal(size = N)
#     W = np.cumsum(W)*np.sqrt(dt) # standard brownian motion
#     X = (mu-0.5*sigma**2)*t + sigma*W
#     S = S0*np.exp(X) # geometric brownian motion
#     return S

threads = np.array(list(range(1, 65)))

chunk_size = np.array([1024, 128, 16, 64, 32, 8, 32, 32, 32, 16, 8, 16, 16, 16, 16, 16, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8,
                       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                       8, 8, 8, 8, 8, 8])

exec_time = np.array(
    [79.6, 40.5, 28.3, 21.6, 17.3, 14.8, 12.9, 11.2, 10, 9.2, 8.3, 7.7, 7.1, 6.7, 6.3, 6.1, 5.8, 5.6, 5.3, 5.1, 5, 4.9,
     4.7, 4.7, 4.7, 4.5, 4.4, 4.2, 4.1, 4, 3.9, 3.9, 3.7, 3.7, 3.7, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.2, 3.2, 3.2, 3.2,
     3.2, 3.2, 3.2, 3.1, 3.1, 3, 3, 3.1, 3, 3.1, 2.9, 3.2, 3.2, 3, 2.9, 2.9, 2.9, 2.9, 3])

fig = go.Figure(data=go.Scatter3d(
    x=threads, y=chunk_size, z=exec_time,
    marker=dict(
        size=4,
        color=exec_time,
        colorscale='rainbow',
    ),
    line=dict(
        color='darkblue',
        width=2
    )
))

fig.update_layout(
    title='Execution Time of ChunkSize vs Thread Count for Prime Finder',
    width=1200,
    height=900,
    autosize=False,
    scene=dict(
        xaxis_title='Thread (#)',
        yaxis_title='Chunk Size (n)',
        zaxis_title='Execution time (ms)',
        #     camera=dict(
        #         up=dict(
        #             x=0,
        #             y=1,
        #             z=0
        #         ),
        #         eye=dict(
        #             x=0,
        #             y=1.0707,
        #             z=.98,
        #         )
        #     ),
        #     aspectratio=dict(x=1, y=1, z=1.2),
        #     aspectmode='manual'
        # ),
    )
)

fig.show()
