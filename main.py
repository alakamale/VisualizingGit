import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from queries import data1, data2, data3, data4, count, x_pos, language
import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

## Github-Repo-Sizes
#data1 = pd.read_csv('')
app.layout = html.Div(children=[
    html.H1(children='Github Archive', style = {'text-align' : 'center'}),
    html.Div(
        dcc.Graph(
                    id='trending-language-time',
                    figure={
                                'data': [go.Scatter(x=list(data4.Date),
                                        y=list(data4.Python), name='Python'),

                                        go.Scatter(x=list(data4.Date),
                                        y=list(data4.HTML), name='HTML'),

                                        go.Scatter(x=list(data4.Date),
                                        y=list(data4.Java), name='Java'),

                                        go.Scatter(x=list(data4.Date),
                                        y=list(data4.Ruby), name='Ruby'),

                                        go.Scatter(x=list(data4.Date),
                                        y=list(data4.JavaScript), name='JavaScript')],
                                'layout' : go.Layout(
                                            title = 'Trending Languages Watchcount over time', titlefont = dict(size = 30, color='#177a21'),
                                            xaxis = {'rangeselector': {'buttons': [{'count': 1,
                                                    'label': '1m',
                                                    'step': 'month',
                                                    'stepmode': 'backward'},
                                                    {'count': 6, 'label': '6m', 'step': 'month', 'stepmode': 'backward'},
                                                    {'count': 1, 'label': 'YTD', 'step': 'year', 'stepmode': 'todate'},
                                                    {'count': 1, 'label': '1y', 'step': 'year', 'stepmode': 'backward'},
                                                    {'step': 'all'}]},
                                                    'rangeslider': {'visible': True},
                                                    'type': 'date'},
                                            #yaxis = {'title' : 'Size'}        
                                                    )
                            },
                    style={'width': '1800'}

                ), style={'display': 'inline-block', 'width':'1800'},
            ),
    html.Div(
        dcc.Graph(
                    id='Repo-Sizes',
                    figure={
                                'data': [
                                go.Scatter(x=data1.index,
                                           y=data1['size'],
                                          mode = 'lines+markers',
                                          )
                                        ],
                                'layout' : go.Layout(
                                            title = 'Sizes of Github Repos on Head Branch in MBs', titlefont = dict(size = 30, color='#177a21'),
                                            xaxis = {'title' : 'Index'},
                                            yaxis = {'title' : 'Size'}        
                                                    )
                            },
                    style={'width': '800'}

                ), style={'display': 'inline-block'},
            ),
    html.Div(
        dcc.Graph(
                    id='trending-repo',
                    figure={
                            'data': [
                                go.Bar(x=data2.watch_count,
                                       y=data2.repo_name,
                                       orientation = 'h',
                                       marker = {'color' : [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150], 'colorscale' : 'Reds', 'reversescale' : True},

                                      )
                                    ],
                            'layout': go.Layout(
                                                title = 'Trending Github Repositories',
                                                titlefont = dict(size = 30, color='#177a21'),
                                                xaxis = {'title' : 'Watch Count'},         
                                                yaxis = {'title' : 'Repository Name'},
                                                margin = go.Margin( l = 250 , r = 50)
                                               )
                            },
                    style={'width': '1000'}
                  ), style={'display': 'inline-block'}, 
            ),
    html.Div(
        dcc.Graph(
                    id='trending-language',
                    figure={
                            'data': [
                                go.Bar(x=x_pos,
                                       y=count,
                                       marker = {'color' : [0,1,2,3,4,5,6,7,8,9], 'colorscale' : 'YlOrRd' }
                                      )
                                    ],
                            'layout': go.Layout(
                                                title = 'Language Popularity Score',
                                                titlefont = dict(size = 30, color='#177a21'),
                                                xaxis = {'tickvals' : x_pos, 'ticktext' : language, 'tickmode' : 'array'},         
                                                #yaxis = {'title' : 'Repository Name'},
                                                margin = go.Margin( l = 250 )
                                               )
                            },
                    style={'width': '800'}
                  ), style={'display': 'inline-block'}, 
            ),
    html.Div(
        dcc.Graph(
                    id='java-repo',
                    figure={
                            'data': [
                                 go.Bar(x=data3.num_commits,
                                        y=data3.repo_name,
                                        orientation = 'h',
                                        marker = {'color' : [0,1], 'colorscale' : 'RdBu' }
                                        )
                                    ],
                            'layout': go.Layout(
                                                title = 'Top Java Github Repositories <br> by their commits Count',
                                                titlefont = dict(size = 30, color='#177a21'),
                                                xaxis = {'title' : 'num_commits'},
                                                yaxis = {'title' : 'repo_name'},
                                                margin = go.Margin( l = 250 )
                                                )
                            },
                    style={'width': '500'}
                  ), style={'display': 'inline-block'}, 
            ),





])


#fig = go.Figure(data=[data], layout=layout1)
#iplot(fig)


if __name__ == '__main__':
    app.run_server(debug=True)
