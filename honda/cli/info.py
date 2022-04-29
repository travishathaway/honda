from .display.table import print_no_header_table

doc = '''
     active environment : None
            shell level : 0
       user config file : /Users/travishathaway/.condarc
 populated config files : /Users/travishathaway/.condarc
          conda version : 4.12.0.post41+6a1493bee
    conda-build version : 3.21.8
         python version : 3.10.4.final.0
       virtual packages : __osx=12.2.1=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /Users/travishathaway/opt/conda_x86_64  (writable)
      conda av data dir : /Users/travishathaway/opt/conda_x86_64/etc/conda
  conda av metadata url : None
           channel URLs : https://conda.anaconda.org/conda-forge/osx-64
                          https://conda.anaconda.org/conda-forge/noarch
                          file:///Users/travishathaway/opt/conda_x86_64/conda-bld/osx-64
                          file:///Users/travishathaway/opt/conda_x86_64/conda-bld/noarch
                          file:///Users/travishathaway/dev/recipes/.channel/osx-64
                          file:///Users/travishathaway/dev/recipes/.channel/noarch
          package cache : /Users/travishathaway/opt/conda_x86_64/pkgs
                          /Users/travishathaway/.conda/pkgs
       envs directories : /Users/travishathaway/opt/conda_x86_64/envs
                          /Users/travishathaway/.conda/envs
               platform : osx-64
             user-agent : conda/4.12.0.post41+6a1493bee requests/2.27.1 CPython/3.10.4 Darwin/21.3.0 OSX/12.2.1
                UID:GID : 501:20
             netrc file : None
           offline mode : False
'''


def info():
    print_no_header_table('honda info', {
        'active_environment': 'n/a',
        'something_else': 'baladf asdf asdf ads f',
        'user-agent': 'conda/4.12.0.post41+6a1493bee requests/2.27.1 CPython/3.10.4 Darwin/21.3.0 OSX/12.2.1',
        'channel_urls': [
            'https://conda.anaconda.org/conda-forge/osx-64',
            'https://conda.anaconda.org/conda-forge/noarch',
            'file:///Users/travishathaway/opt/conda_x86_64/conda-bld/osx-64',
            'file:///Users/travishathaway/opt/conda_x86_64/conda-bld/noarch',
            'file:///Users/travishathaway/dev/recipes/.channel/osx-64',
            'file:///Users/travishathaway/dev/recipes/.channel/noarch',
        ]
    })
