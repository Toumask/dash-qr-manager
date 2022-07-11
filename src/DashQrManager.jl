
module DashQrManager
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.3"

include("jl/''_dashqrgenerator.jl")
include("jl/''_dashqrreader.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_qr_manager",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_qr_manager.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_qr_manager.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
