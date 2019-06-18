import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import no_update


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]
)


app.title = 'Russell Romney'
app.config['suppress_callback_exceptions'] = True
server = app.server


app.layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.Div('This is the blog of Russell',id='content'),
                dbc.Button('Change name to uppercase',id='change',n_clicks=0)
            ]
        )
    )
)

@app.callback(
    [Output('content','children'),
     Output('change','children')],
    [Input('change','n_clicks')]
)
def change_content(n):
    if n%2:
        name = 'Russell'
        case = 'lower'
    else:
        name = 'RUSSELL'
        case = 'lower'
    return 'This is the blog of '+name, 'Change name to case'.format(case)

