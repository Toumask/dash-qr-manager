import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {QrReader} from "react-qr-reader";


/**
 * Dash QR Code Reader
 * for more information: https://www.npmjs.com/package/react-qr-reader
 */

export default class DashQrReader extends Component {

    render() {
        const {
            id,
            style,
            videoId,
            scanDelay,
            className,
            containerStyle,
            videoContainerStyle,
            videoStyle,
            setProps
        } = this.props;

        return (
            <div id={id}>
                <QrReader
                    onResult={(result, error) => {
                        if (!!result) {
                            console.log(result)
                            console.log(result?.text)
                            this.props.setProps({result : result?.text})
                          }
                          if (!!error) {
                            console.info(error)
                          }
                      }}
                    style={style}
                    videoId={videoId}
                    scanDelay={scanDelay}
                    className={className}
                    containerStyle={containerStyle}
                    videoContainerStyle={videoContainerStyle}
                    videoStyle={videoStyle}
                />
            </div>
        );
    }
}

DashQrReader.defaultProps = {};

DashQrReader.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * The style of the QR code.
     */
    style: PropTypes.object,
    /**
     * The ID for the video element
     */
    videoId: PropTypes.string,
    /**
     * The scan period for the QR hook
     */
    scanDelay: PropTypes.number,
    /**
     * ClassName for the container element.
     */
    className: PropTypes.string,
    /**
     * Style object for the container element.
     */
    containerStyle: PropTypes.object,
    /**
     *  Style object for the video container element.
     */
    videoContainerStyle: PropTypes.object,
    /**
     *    Style object for the video element.
     */
    videoStyle: PropTypes.object,
    /**
     *   decoded data
     */
    result: PropTypes.string,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
