import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

data = pd.read_csv('output.csv')
app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1("Sales Data Visualization"),  # Header
        dcc.Graph(id="sales-chart")  # Line chart
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("sales-chart", "id")
)
def update_chart(_):
    figure = {
        "data": [
            {
                "x": data["date"],  # x-axis: date
                "y": data["sales"],  # y-axis: sales
                "type": "line"
            }
        ],
        "layout": {
            "title": "Sales Trend",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Sales"}
        }
    }
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
