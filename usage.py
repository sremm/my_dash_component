import dash
import dash_html_components as html
from dash.dependencies import Input, Output

import my_dash_component

app = dash.Dash(__name__)

app.layout = html.Div(
    [my_dash_component.AnotherComponent(id="input", value="my-value", label="my-label"), html.Div(id="output")]
)


@app.callback(Output("output", "children"), [Input("input", "value")])
def display_output(value):
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
