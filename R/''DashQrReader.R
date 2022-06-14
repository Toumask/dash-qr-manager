# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DashQrReader <- function(id=NULL, className=NULL, containerStyle=NULL, result=NULL, scanDelay=NULL, style=NULL, videoContainerStyle=NULL, videoId=NULL, videoStyle=NULL) {
    
    props <- list(id=id, className=className, containerStyle=containerStyle, result=result, scanDelay=scanDelay, style=style, videoContainerStyle=videoContainerStyle, videoId=videoId, videoStyle=videoStyle)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashQrReader',
        namespace = 'dash_qr_manager',
        propNames = c('id', 'className', 'containerStyle', 'result', 'scanDelay', 'style', 'videoContainerStyle', 'videoId', 'videoStyle'),
        package = 'dashQrManager'
        )

    structure(component, class = c('dash_component', 'list'))
}
