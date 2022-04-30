from .display.table import print_no_header_table


def info():
    print_no_header_table(
        "honda info",
        {
            "active_environment": "n/a",
            "something_else": "baladf asdf asdf ads f",
            "user-agent": "conda/4.12.0.post41+6a1493bee requests/2.27.1 CPython/3.10.4 Darwin/21.3.0 OSX/12.2.1",
            "channel_urls": [
                "https://conda.anaconda.org/conda-forge/osx-64",
                "https://conda.anaconda.org/conda-forge/noarch",
                "file:///Users/travishathaway/opt/conda_x86_64/conda-bld/osx-64",
                "file:///Users/travishathaway/opt/conda_x86_64/conda-bld/noarch",
                "file:///Users/travishathaway/dev/recipes/.channel/osx-64",
                "file:///Users/travishathaway/dev/recipes/.channel/noarch",
            ],
        },
    )
