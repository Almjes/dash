# importando as bibliotecas
import pandas as pd
import dash_bootstrap_components as dbc
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

df_limpo = pd.read_csv('C:/Users/Jessica/Downloads/projetos_Dash/df_ver1.csv')
print(df_limpo.head())
print(df_limpo.columns)
print(df_limpo.info())

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SOLAR])
# ------------------------------------layout-------------------------------------------------------------------------------
app.layout = html.Div([
    dbc.Button("Sucesso",color="success",className="nr-1"),
    dbc.Row(
        [
            dbc.Col(dcc.Dropdown(id='my_dropdown',
                    options=[{'label': x, 'value': x} for x in sorted(df_limpo.Setor.unique())],
                    value='Financeiro',),
                    width={'size': 6, "offset": 3}
                    )


        ]
    ),

    dbc.Row(
            [
            dbc.Col(dcc.Graph(id='pie-graph', figure={}, className='five columns'),

                    width=4, lg={'size': 6, "offset": 0, 'order': 'first'}


                  ),

            dbc.Col(dcc.Graph(id="the_graph", figure={}, clickData=None, hoverData=None,
                  # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,  # True, False
                      'scrollZoom': True,  # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,  # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                  },
                  className='five columns'
                  ),
                   width=4, lg={'size': 6, "offset": 0, 'order': 'last'}

                  )
            ]
         )

])




# ------------------------------------------------------------callback-------------------------------------------------
@app.callback(Output(component_id="the_graph", component_property="figure"),
              [Input(component_id="my_dropdown", component_property="value")])
def update_graph(setor):
    print(setor)
    dff = df_limpo[df_limpo.Setor == setor]
    fig = px.line(dff, x='data', y='value', color='Cod_acao',custom_data=['Cod_acao', 'Setor', 'Volume'])
    fig.update_traces(mode='lines+markers')
    return fig
# ------------------------------------------------------------callback------------------------------------------------

@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id="the_graph", component_property='hoverData'),
    Input(component_id="the_graph", component_property='clickData'),
    Input(component_id="the_graph", component_property='selectedData'),
    Input(component_id="my_dropdown", component_property='value'))

def update_side_graph(hov_data, clk_data, slct_data,setor):
    if hov_data is None:
        dff2 = df_limpo[df_limpo.Setor == setor]
        dff2 = dff2[dff2.data == '2020-04-20']
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='Volume', names='Cod_acao',
                      title='Volume em 20-04-2020')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df_limpo[df_limpo.Setor == setor]
        print(hov_data['points'][0]['x'])
        print(dff2)
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.data == hov_year]
        fig2 = px.pie(data_frame=dff2, values='Volume', names='Cod_acao', title=f'Volume em: {hov_year}')
        return fig2




if __name__ == '__main__':
    app.run_server(
        port=8050,

    )