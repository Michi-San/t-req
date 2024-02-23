import dash
from dash import html, dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

import warnings
import pandas as pd 
pd.set_option("display.max_columns", 100)
warnings.filterwarnings("ignore")

from helpers.layout_utils import *

from views import login as LoginScreen, azure_ticket_landing as AzureLandingScreen

from app import app, server, app_server, cache, cacheconfig
# App layout
base_layout = html.Div(
    [
        get_login_header(),
        get_logo_header(),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', style=base_div_style),
        dcc.Store(id="currentpage_store", storage_type="session"),
    ],
    style=CONTAINER_STYLE,
)

validation_layout = html.Div(
    [
        base_layout,
        LoginScreen.login_landing,
        AzureLandingScreen.layout_azure_landing
        
    ]
)

app.validation_layout = validation_layout
app.layout = base_layout


# Callback to render different pages based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page_content(pathname):
    if pathname in ["/Treq/"]:
        return LoginScreen.login_landing()
    
    elif pathname in ["/Treq/azure-landing"]:
        return AzureLandingScreen.layout_azure_landing()
    
    else:
        return None


if __name__ == '__main__':
    app.run(port=8000)
