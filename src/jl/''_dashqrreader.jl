# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashqrreader

"""
    ''_dashqrreader(;kwargs...)

A DashQrReader component.
Dash QR Code Reader
for more information: https://www.npmjs.com/package/react-qr-reader
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): ClassName for the container element.
- `containerStyle` (Dict; optional): Style object for the container element.
- `result` (String; optional): decoded data
- `scanDelay` (Real; optional): The scan period for the QR hook
- `style` (Dict; optional): The style of the QR code.
- `videoContainerStyle` (Dict; optional): Style object for the video container element.
- `videoId` (String; optional): The ID for the video element
- `videoStyle` (Dict; optional): Style object for the video element.
"""
function ''_dashqrreader(; kwargs...)
        available_props = Symbol[:id, :className, :containerStyle, :result, :scanDelay, :style, :videoContainerStyle, :videoId, :videoStyle]
        wild_props = Symbol[]
        return Component("''_dashqrreader", "DashQrReader", "dash_qr_manager", available_props, wild_props; kwargs...)
end

