# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashQrReader(Component):
    """A DashQrReader component.
Dash QR Code Reader
for more information: https://www.npmjs.com/package/react-qr-reader

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
    Style object for the video element."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_qr_manager'
    _type = 'DashQrReader'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, videoId=Component.UNDEFINED, scanDelay=Component.UNDEFINED, className=Component.UNDEFINED, containerStyle=Component.UNDEFINED, videoContainerStyle=Component.UNDEFINED, videoStyle=Component.UNDEFINED, result=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'containerStyle', 'result', 'scanDelay', 'style', 'videoContainerStyle', 'videoId', 'videoStyle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'containerStyle', 'result', 'scanDelay', 'style', 'videoContainerStyle', 'videoId', 'videoStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashQrReader, self).__init__(**args)
