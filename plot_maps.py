import plotly.graph_objects as go

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df_periods = pd.read_csv('periods_for_city.txt')
df_cities = pd.read_csv('city_attributes.csv')

df_cities['Rank1'] = df_periods['Rank1']
print(df_cities.head())

colors = ['rgb(76,0,153)', 'rgb(204,102,0)', 'rgb(0,253,15)', 'rgb(133,113,181)']
# months = {6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept'}
months = {6: 'Reg', 7: 'July', 8: 'Aug', 9: 'Sept'}

fig = go.Figure()

israel = df_cities[df_cities['Country'] == 'Israel']

america = df_cities[df_cities['Country'] != 'Israel']


# scatter chart for outbreak size
for i in range(america.shape[0]):
    fig.add_trace(go.Scattergeo(
        lon=america['Longitude'],
        lat=america['Latitude'],
        # text=df_cities['City'],
        # name=df_cities['Rank1'].astype(str),
        marker=dict(
            size=5,
            # color=colors[i - 6],
            line_width=0),
        geo='geo'
    )
    )

    # scatter chart for outbreak size
    for i in range(israel.shape[0]):
        fig.add_trace(go.Scattergeo(
            lon=israel['Longitude'],
            lat=israel['Latitude'],
            # text=df_cities['City'],
            # name=df_cities['Rank1'].astype(str),
            marker=dict(
                size=5,
                # color=colors[i - 6],
                line_width=0),
            geo='geo2'

        )
        )

# df_sept = df.query('Month == 9')
# fig.data[0].update(text=df_sept['Value'].map('{:.0f}'.format).astype(str) + ' ' + \
#                         df_sept['Country'],
#                    mode='markers+text',
#                    textposition='bottom center')
#
# fig.add_trace(go.Choropleth(
#     locationmode='country names',
#     locations=df_cities['Country'],
#     z=df_cities['Value'],
#     text=df_cities['Country'],
#     colorscale=[[0, 'rgb(0, 0, 0)'], [1, 'rgb(0, 0, 0)']],
#     autocolorscale=False,
#     showscale=False,
#     geo='geo2'
# ))
# fig.add_trace(go.Scattergeo(
#     lon=[21.0936],
#     lat=[7.1881],
#     text=['Africa'],
#     mode='text',
#     showlegend=False,
#     geo='geo2'
# ))

fig.update_layout(
    title_text='Ebola cases reported by month in West Africa 2014<br> \
Source: <a href="https://data.hdx.rwlabs.org/dataset/rowca-ebola-cases">\
HDX</a>',
    geo=dict(
        resolution=50,
        scope='north america',
        showframe=False,
        showcoastlines=True,
        showland=True,
        landcolor="lightgray",
        countrycolor="white",
        coastlinecolor="white",
        projection_type='equirectangular',
        lonaxis_range=[-123.0, -55.0],  # horizontal
        lataxis_range=[23.0, 53.0],  # vertical
        domain=dict(x=[0, 0.6], y=[0, 0.6])
    )
    ,
    geo2=dict(
        scope='asia',
        showframe=False,
        showland=True,
        landcolor="lightgray",
        showcountries=False,
        lonaxis_range=[34.0, 38.0],  # horizontal
        lataxis_range=[29.0, 34.0],  # vertical
        domain=dict(x=[0, 1], y=[0, 1]),

        bgcolor='rgba(255, 255, 255, 0.0)',
    ),
    legend_traceorder='reversed'
)

fig.show()
