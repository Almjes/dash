from random import randint
from dash.dependencies import Input, Output
import dash_core_components as dcc
from dash_html_components import Div, P, H1, H2
from dash import Dash
from dash_core_components import Graph, Dropdown, Slider, Checklist

n = 20
database = {
    "index": list(range(n)),
    "maiores": [randint(1, 1000) for _ in range(n)],
    "menores": [randint(1, 1000) for _ in range(n)],
    "bebes": [randint(1, 1000) for _ in range(n)]

}
app = Dash(__name__)  ## aqui é uma conversão para ele usar proprio nome do arquivo

app.layout = Div(  # A lista Children diz para Div esse componetes declarados dentro da lista estão dentro dele

    children=[
        H1('Olá mundo!!!'),
        P("Vivendo e aprendendo a jogar nem sempre gando nem sempre perdendo,ams aprendendo jogar."),
        H2('Let go!!!'),

        Checklist(
            id="meu_ckeck_list",
            options=[
                {'label': "Menores", 'value': 'menores'},
                {'label': "Maiores", 'value': 'maiores'},
                {'label': "Bebes", 'value': 'bebes'}
            ],
            value=['menores']  # valor padrão

        ),

        Graph(
            id='meu_grafico',
            config={'displayModeBar': False},

        )

    ]
)


@app.callback(
    Output('meu_grafico', 'figure'),
    [Input("meu_ckeck_list", "value")]

)
def my_callback(input_data):
    grafico = {

        'data': []
    }
    for x in input_data:
        grafico['data'].append(
            {
                "y": database[x],
                "x": database["index"],
                "name": x
            },

        )
        return grafico


app.run_server(debug=True)