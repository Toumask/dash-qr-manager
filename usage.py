import dash_qr_manager as dqm
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dqm.DashQrGenerator(
        id='qr-code',
        data='Hallo',
        framed=True,
    ),
    dqm.DashQrReader(
        id='qr-code-reader',
        style={'width': '50%'}
    ),
    html.Div(id='output'),
    html.Div(id='output2')
])


@app.callback(Output('output', 'children'), [Input('qr-code', 'data')])
def display_output(value):
    return 'You have entered {}'.format(value)


@app.callback(Output('output2', 'children'), Input('qr-code-reader', 'result'))
def code(result):
    print(result)
    return result


if __name__ == '__main__':
    app.run_server(debug=True)
