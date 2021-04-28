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

df_limpo = pd.read_csv('C:/Users/Jessica/Downloads/projetos_Dash/df_limpo.csv')

app = dash.Dash(__name__)
# ------------------------------------layout-------------------------------------------------------------------------------
app.layout = html.Div([

    dcc.Dropdown(id='my_dropdown',
                 options=[{'label': x, 'value': x} for x in sorted(df_limpo.Setor.unique())],
                 value='Financeiro',

                 ),

    html.Div([

        dcc.Graph(id="the_graph")

    ]),

])


# ------------------------------------------------------------callback-------------------------------------------------
@app.callback(Output(component_id="the_graph", component_property="figure"),
              [Input(component_id="my_dropdown", component_property="value")])
def update_graph(setor):
    print(setor)
    dff = df_limpo[df_limpo.Setor == setor]
    fig = px.line(dff, x='data', y='value', color='Cod_acao')

    return fig


if __name__ == '__main__':
    app.run_server(
        port=8050,

    )