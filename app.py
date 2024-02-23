import dash
import flask

import dash_auth
import dash_bootstrap_components as dbc
import os


### SERVER ###
server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    title="T-Req's",
    update_title="T-Req's is working",
    serve_locally=True,
    prevent_initial_callbacks=False,
    routes_pathname_prefix="/Treq/",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app_server = app.server

server = app.server
app.config.suppress_callback_exceptions = True
###########################################################################################################################

from flask_caching import Cache

cacheconfig = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory",
    "CACHE_THRESHOLD": 1000,
}

cache = Cache(server, config=cacheconfig)
###########################################################################################################################
