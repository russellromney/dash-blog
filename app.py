import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import no_update


from settings import (
    config_name,
    config_description,
    config_homepage,
    config_github,
    config_linkedin,
    server_secret_key
)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]
)


app.title = 'Russell Romney'
app.config['suppress_callback_exceptions'] = True

server = app.server
server.secret_key = server_secret_key

app.layout =  html.Div(
    [
        # navbar
        dbc.Navbar(
            [
                # logo and name
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src='/assets/logo-small.png',height='50px')),
                            #dbc.Col(dbc.NavbarBrand('Russell Romney',className='ml-2'))
                        ],
                        align='center',
                        no_gutters=True
                    ),
                    href=config_homepage
                )
            ],
            color='light',
        ), # end navbar
        
        # TODO
        # location manager
        dcc.Location(id='url'),
        
        # body
        dbc.Container(
            dbc.Row(
                [
                    # TODO
                    # store for cookies
                    dcc.Store(id='browser-store'),
                    
                    # content engine
                    dbc.Col(
                        [
                            dbc.Jumbotron(
                                [
                                    html.H1('The website of Russell Romney',className='display-3'),
                                    html.P(
                                        "Ruminations, etc.",
                                        className='lead'
                                    ),
                                    html.Hr(className='my-2'),
                                    html.A(dbc.Button('About Me',color='primary'),href='/about')
                                ]
                            ),
                            
                            # TODO
                            # recommended articles

                            # TODO
                            # comments (commento)
                        ],
                        width=8
                    ), # end content engine
                    
                    # sidebar
                    dbc.Col(
                            [
                                # me
                                dbc.Card(
                                    [
                                        dbc.CardImg(src='assets/him.png',top=True),
                                        dbc.CardBody(
                                            [
                                                # name
                                                html.H4(config_name,className='card-title'),
                                                # description
                                                html.P(
                                                    config_description,
                                                    className='card-text'
                                                ),
                                            ]
                                        ),
                                    ]
                                ), # end of me card

                                html.Br(),

                                # TODO
                                # social
                                dbc.Card(
                                    [
                                        dbc.CardBody(
                                            [
                                                html.H4('Connect',className='card-title'),
                                                html.A(
                                                    'GitHub',
                                                    href=config_github,
                                                    className='card-link',
                                                    target='_blank'
                                                ),
                                                html.A(
                                                    'LinkedIn',
                                                    href=config_linkedin,
                                                    className='card-link',
                                                    target='_blank'
                                                ),
                                                
                                            ]
                                        )
                                    ]
                                ), # end social card

                                html.Br(),

                                # TODO
                                # posts card
                                dbc.Card(
                                    dbc.CardLink(
                                        [
                                            dbc.CardImg(src='/assets/logo.png'),
                                            dbc.CardImgOverlay('This is my swamp',className='card-title'),
                                        ],
                                        href='#'
                                    )
                                ), # end posts card

                                html.Br(),


                            ],
                        width=3
                    ), # end sidebar
                ]
            )
        ), # end body
    ],
    style=dict(width='100%')
)