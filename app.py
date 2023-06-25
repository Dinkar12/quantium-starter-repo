import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

data = pd.read_csv('output.csv')
app = dash.Dash(__name__, external_stylesheets=["style.css"])
app.layout = html.Div(
    children=[
        html.H1("Sales Data Visualization"),  # Header
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            labelStyle={"display": "inline-block"}
        ),
        dcc.Graph(id="sales-chart")  # Line chart
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data  # Show all data
    else:
        filtered_data = data[data["region"] == selected_region]

    figure = {
        "data": [
            {
                "x": filtered_data["date"],  # x-axis: date
                "y": filtered_data["sales"],  # y-axis: sales
                "type": "line"
            }
        ],
        "layout": {
            "title": f"Sales Trend - Region: {selected_region.capitalize()}",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Sales"}
        }
    }
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
