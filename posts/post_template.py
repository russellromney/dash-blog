import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from elements import (
    color,
    color2
)

content = dbc.Row(dbc.Col(
    [
            dcc.Markdown(
'''
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."
'''
            ),
            
            html.Br(),
            
            dbc.Card(dbc.CardImg(src='https://picsum.photos/500/300')),
            
            html.Br(),
            
            dcc.Markdown(
'''
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."
'''
            ),
            html.Br()
    ]
))