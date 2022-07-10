import dash_qr_manager as dqm
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dqm.DashQrGenerator(
            id='qr-code',
            data='http://example.com/',
            framed=True,
        ),
        dqm.DashQrReader(
            id='qr-code-reader',
            style={'width': '50%'}
        ),
        html.Div(id='qr-code-data')
    ]
)


@app.callback(
    Output('qr-code-data', 'children'),
    Input('qr-code-reader', 'result')
)
def code(qr_code_data):
    return qr_code_data


if __name__ == '__main__':
    app.run_server(debug=True)
