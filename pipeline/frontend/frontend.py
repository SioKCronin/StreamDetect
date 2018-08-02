# _*_ coding: utf-8 _*_

import os
import redis

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask_caching import Cache
from kafka import SimpleProducer, KafkaClient

from datetime import datetime
import time

app = dash.Dash(__name__)
server = app.server

# Establish Redis cache connection
CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

# Config settings
app.config.suppress_callback_exceptions = True
timeout = 20

# App layout
app.layout = html.Div(children=[
    html.H1(children='Sift: Realtime streaming search'),
    dcc.Dropdown(
        id='input-1-state', 
        options=[{'label': s[0], 'value': str(s[1])}
                 for s in [["data", "data"], ["engineering", "engineering"]]],
        value=['data', 'engineering'],
        multi=True
    ),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
])

@app.callback(
    Output('flask-cache-memoized-children', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-1-state', 'value')])
@cache.memoize(timeout=timeout) # in seconds

def update_output_div(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)

if __name__ == '__main__':
    app.run_server(debug=True)
