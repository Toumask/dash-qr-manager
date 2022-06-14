# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashqrgenerator

"""
    ''_dashqrgenerator(;kwargs...)

A DashQrGenerator component.
Dash QR Code Generator
for more information: https://www.npmjs.com/package/react-google-qrcode
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (String; optional): The data to encode.
- `framed` (Bool; optional): Adds a frame to the image
- `size` (Real; optional): Image size in pixels (width x height). Min value: 30, Max value: 547
- `style` (Dict; optional): The style of the QR code.
"""
function ''_dashqrgenerator(; kwargs...)
        available_props = Symbol[:id, :data, :framed, :size, :style]
        wild_props = Symbol[]
        return Component("''_dashqrgenerator", "DashQrGenerator", "dash_qr_manager", available_props, wild_props; kwargs...)
end

