<p>
    <img src="https://badgen.net/pypi/license/dash-qr-manager">
    <a href="https://pypi.org/project/dash-mantine-components/">
    <img src="https://badgen.net/pypi/v/dash-qr-manager">
    </a>
    <img src="https://static.pepy.tech/personalized-badge/dash-qr-manager?period=total&units=international_system&left_color=black&right_color=yellowgreen&left_text=Downloads">
</p>

Dash QR Manger is a Dash component based on [react-google-qrcode](https://www.npmjs.com/package/react-google-qrcode) and [react-qr-reader](https://www.npmjs.com/package/react-qr-reader) for creating and reading QR codes.

Installation
======
```bash
pip install dash-qr-manager
```


Usage
======
Creating QR code
-----
```python
import dash_qr_manager as dqm
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dqm.DashQrGenerator(
            id='qr-code',
            data='http://example.com/',
            framed=True,
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

Reading QR code
-----
```python
import dash_qr_manager as dqm
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
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
```

Documentation
======
DashQrGenerator
-----
```
Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- data (string; optional):
    The data to encode.

- framed (boolean; optional):
    Adds a frame to the image.

- size (number; optional):
    Image size in pixels (width x height). Min value: 30, Max value:
    547.

- style (dict; optional):
    The style of the QR code.

for more information: https://www.npmjs.com/package/react-google-qrcode
```

DashQrReader
-----
```
Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    ClassName for the container element.

- containerStyle (dict; optional):
    Style object for the container element.

- result (string; optional):
    decoded data.

- scanDelay (number; optional):
    The scan period for the QR hook.

- style (dict; optional):
    The style of the QR code.

- videoContainerStyle (dict; optional):
    Style object for the video container element.

- videoId (string; optional):
    The ID for the video element.

- videoStyle (dict; optional):
    Style object for the video element.

for more information: https://www.npmjs.com/package/react-qr-reader
```