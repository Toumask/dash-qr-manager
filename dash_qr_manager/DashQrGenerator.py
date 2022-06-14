# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashQrGenerator(Component):
    """A DashQrGenerator component.
Dash QR Code Generator
for more information: https://www.npmjs.com/package/react-google-qrcode

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
    The style of the QR code."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_qr_manager'
    _type = 'DashQrGenerator'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, size=Component.UNDEFINED, framed=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'framed', 'size', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'framed', 'size', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashQrGenerator, self).__init__(**args)
