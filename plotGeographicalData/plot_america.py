import plotly.graph_objects as go

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df_periods = pd.read_csv('periods_for_city.txt')
df_cities = pd.read_csv('city_attributes.csv')

df_cities['Rank1'] = df_periods['Rank1']
# print(df_cities.head())

# colors = ['rgb(76,0,153)', 'rgb(204,102,0)', 'rgb(0,253,15)', 'rgb(133,113,181)']
# months = {6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept'}
months = {6: 'Reg', 7: 'July', 8: 'Aug', 9: 'Sept'}

fig = go.Figure()

israel = df_cities[df_cities['Country'] == 'Israel']

america = df_cities[df_cities['Country'] != 'Israel']
colors = {12: 'rgb(227,23,52)', 24: 'rgb(255,200,128)', 3: 'rgb(31,33,32)'}

ranks = {24: '24', 12: '12', 3: '3'}
print(america.Rank1.unique())
x = 0
# scatter chart for outbreak size
for i in america.Rank1.unique():
    df_Rank = america.query('Rank1 == %d' % i)
    print(df_Rank)
    fig.add_trace(go.Scattergeo(
        lon=df_Rank['Longitude'],
        lat=df_Rank['Latitude'],
        text=df_Rank['Rank1'],
        name=ranks[i],
        marker=dict(
            size=15,
            color=colors[i],
            line_width=0),
        geo='geo'
        )
    )
    x += 1

fig.update_layout(
    title_text="City Weather's Period Distribution",
    geo=dict(
        resolution=50,
        scope='north america',
        showframe=False,
        showcoastlines=True,
        showland=True,
        landcolor="lightgray",
        countrycolor="whitesmoke",
        coastlinecolor="aqua",
        projection_type='equirectangular',
        # lonaxis_range=[-126.0, -55.0],  # horizontal
        # lataxis_range=[23.0, 53.0],  # vertical
        domain=dict(x=[0, 1], y=[0, 1])
    )
)

fig.show()
