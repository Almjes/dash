# importando as bibliotecas
import pandas as pd
import pandas.util.testing as tm
from time import sleep
from selenium import webdriver
import plotly.express as px
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
#sns.set()
import random
import plotly.express as px
import pandas.util.testing as tm
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

df = pd.read_csv('C:/Users/Jessica/Downloads/projetos_Dash/grupo_setor_2.csv')

app = dash.Dash(__name__)
# ------------------------------------layout-------------------------------------------------------------------------------
app.layout = html.Div([

    dcc.Dropdown(id='my_dropdown',  multi=True,
                 options=[{'label': x, 'value': x} for x in sorted(df.Setor.unique())],
                 value=['Financeiro','Petróleo']

                 ),

    html.Div([

        dcc.Graph(id="the_graph",
                  config={
                      'staticPlot': False,  # True, False
                      'scrollZoom': True,  # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,  # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                  },

                  )

    ]),

])


# ------------------------------------------------------------callback-------------------------------------------------
@app.callback(Output(component_id="the_graph", component_property="figure"),
              [Input(component_id="my_dropdown", component_property="value")])
def update_graph(setor):
    print(setor)
    filter2 = df.Setor.isin(setor)

    fig = px.line(df[filter2], x='data', y='value', color="Setor")


    return fig


if __name__ == '__main__':
    app.run_server(
        port=8050,)
