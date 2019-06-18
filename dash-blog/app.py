import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]
)


app.title = 'Russell Romney'
app.config['suppress_callback_exceptions'] = True
server = app.server