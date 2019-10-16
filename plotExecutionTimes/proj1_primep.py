import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)
threads = np.array(list(range(1, 65)))
exec_time = np.array([81.0, 41.9, 31.7, 22.5, 21.6, 16.9, 14.6, 15.3, 11.6, 12.3, 10.7, 9.8, 11, 8.7, 8.3, 9.2, 8.2, 8,
                      8.6, 7.2, 7.3, 7.2, 7.4, 6.8, 7.1, 6.5, 5.7, 7, 5.8, 5.2, 5.8, 5.7, 4.9, 5.9, 5, 5.3, 4.6, 4.6, 5,
                      5.2, 4.7, 5.2, 4.6, 4.2, 4.8, 4.8, 4.7, 4.4, 4.6, 4.7, 4.7, 4.6, 4.2, 3.9, 4.1, 4.5, 4.2, 3.8,
                      4.3, 4.2, 4, 4.2, 4.3, 4.2])

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=threads, y=exec_time,
                    mode='lines',
                    name='lines'))

fig.update_layout(title='Execution Time vs Thread Count for Prime Finder',
                   xaxis_title='Thread (#)',
                   yaxis_title='Execution time (ms)')
fig.show()
