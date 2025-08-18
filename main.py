# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dash",
#     "dash-mantine-components",
#     "pandas",
#     "plotly",
# ]
# ///
from dash import Dash, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash()

app.layout = dmc.Container([
    dmc.Title('My First App with Data, Graph, and Controls', size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
    dmc.Grid([
        dmc.GridCol([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.GridCol([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)