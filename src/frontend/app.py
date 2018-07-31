# _*_ coding: utf-8 _*_

import os
from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask_caching import Cache
from kafka import SimpleProducer, KafkaClient

app = dash.Dash(__name__)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDUS_URL', '')
})
app.config.suppress_callback_exceptions = True

timeout = 20
app.layout = html.Div(children=[
    html.H1(children='Sift'),
    html.Div(children='''Real-time search of streaming text data'''),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1], 'y': [4], 'type': 'bar', 'name': 'SF'},
                {'x': [1], 'y': [2], 'type': 'bar', 'name': u'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

@app.callback(
    Output('flask-cache-memoized-children', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-1-state', 'value'),
     State('input-2-state', 'value')])
@cache.memoize(timeout=timeout) # in seconds

def update_output_div(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)

if __name__ == '__main__':
    app.run_server(debug=True)
