# Configuration file for lab.

c = get_config()  # noqa

## The default URL to redirect to from `/`
#  Default: '/lab'
c.LabApp.default_url = '/lab/tree/workshops/scipy2023/index.ipynb'

## Set the Access-Control-Allow-Origin header
#
#          Use '*' to allow any origin to access your server.
#
#          Takes precedence over allow_origin_pat.
#  Default: ''
c.ServerApp.allow_origin = '*'
