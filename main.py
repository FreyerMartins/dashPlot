# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dash",
#     "dash-mantine-components",
#     "pandas",
#     "plotly",
# ]
# ///
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Iris samples filtered by petal width"),
        dcc.Graph(id="graph"),
        html.Label("Petal Width:", htmlFor="range-slider"),
        dcc.RangeSlider(
            id="range-slider",
            min=0,
            max=2.5,
            step=0.1,
            marks={0: "0", 2.5: "2.5"},
            value=[0.5, 2],
            tooltip={
                "always_visible": True,
                "placement": "bottom"
            },
        ),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("range-slider", "value"),
)
def update_chart(slider_range):
    low, high = slider_range
    mask = (df.petal_width > low) & (df.petal_width < high)

    fig = px.scatter_3d(
        df[mask],
        x="sepal_length",
        y="sepal_width",
        z="petal_width",
        color="species",
        hover_data=["petal_width"],
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)