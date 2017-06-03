import plotly
plotly.tools.set_credentials_file(username='billyllib', api_key='a6Z5dmrIkL74k5MClKPs')
plotly.tools.set_config_file(world_readable=True,sharing='public')

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go
import csv

csvname='test.csv'
xinput=[]
y1input=[]
y2input=[]
y3input=[]
y4input=[]

f=open(csvname,'r')
for j in csv.reader(f):
    xinput.append(j[0])
    y1input.append(j[3])
    y2input.append(j[1])
    y3input.append(j[2])
    y4input.append(j[4])

f.close()


trace1 = go.Scatter(
    x=xinput,
    y=y1input,
    name='yaxis1 data',
    line = dict(
        color = ('#00DB00'),
        width = 3,
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace2 = go.Scatter(
    x=xinput,
    y=y2input,
    name='yaxis2 data',
    yaxis='y2',
    opacity='1',
    line = dict(
        color = ('#ff7f0e'),
        width = 2.5,
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x=xinput,
    y=y3input,
    name='yaxis3 data',
    yaxis='y3',
    opacity='1',
    line = dict(
        color = ('#d62728'),
        width = 2,
        ) # dash options include 'dash', 'dot', and 'dashdot'
)

data = [trace1, trace2, trace3]
layout = go.Layout(
    title='multiple y-axes example',
    width=1500,
    height=750,
    xaxis=dict(
        domain=[0.15, 0.85],
        range=[0, 80]
    ),
    yaxis=dict(
        title='yaxis title',
        titlefont=dict(
            color='#00DB00'
        ),
        tickfont=dict(
            color='#00DB00'
        ),
        range=[-1200,1200]
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='#ff7f0e'
        ),
        tickfont=dict(
            color='#ff7f0e'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.1,
        range=[-8000,8000]
    ),
    yaxis3=dict(
        title='yaxis4 title',
        titlefont=dict(
            color='#d62728'
        ),
        tickfont=dict(
            color='#d62728'
        ),
        anchor='x',
        overlaying='y',
        side='right',
        range=[-8000,8000]
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multiple-axes-multiple')