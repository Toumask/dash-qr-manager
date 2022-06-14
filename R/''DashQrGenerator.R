# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DashQrGenerator <- function(id=NULL, data=NULL, framed=NULL, size=NULL, style=NULL) {
    
    props <- list(id=id, data=data, framed=framed, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashQrGenerator',
        namespace = 'dash_qr_manager',
        propNames = c('id', 'data', 'framed', 'size', 'style'),
        package = 'dashQrManager'
        )

    structure(component, class = c('dash_component', 'list'))
}
