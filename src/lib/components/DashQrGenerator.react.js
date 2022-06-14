import React, {Component} from 'react';
import PropTypes from 'prop-types';
import QRCode from 'react-google-qrcode';

/**
 * Dash QR Code Generator
 * for more information: https://www.npmjs.com/package/react-google-qrcode
 */

export default class DashQrGenerator extends Component {
    render() {
        const {id, data, style, size, framed, setProps} = this.props;

        return (
            <div id={id} style={style}>
                <QRCode
                    data={data}
                    size={size}
                    framed={framed}
                />
            </div>
        );
    }
}

DashQrGenerator.defaultProps = {};

DashQrGenerator.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * The style of the QR code.
     */
    style: PropTypes.object,
    /**
     * The data to encode.
     */
    data: PropTypes.string,
    /**
     * 	Image size in pixels (width x height). Min value: 30, Max value: 547
     */
    size: PropTypes.number,
    /**
     * 	Adds a frame to the image
     */
    framed: PropTypes.bool,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
