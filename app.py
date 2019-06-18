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
server.secret_key = '^&=mgQ2Ph-Wuq.}U_;HB"_*hw2caxPc7MzXYErh3>s{m!LXgpw9876IJH76b,HJF^&=mgQ2Ph-Wuq.}U_;HB"_*hw2caxPc7MzXYErh3>s{m!LXgpw9876IJH76b,HJF'

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
                    href='http://www.russellromney.me/'
                )
            ],
            color='light',
        ), # end navbar
        
        # location manager
        dcc.Location(id='url'),
        
        # body
        dbc.Container(
            dbc.Row(
                [
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
                            )
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
                                                html.H4('Russell Romney',className='card-title'),
                                                html.P(
                                                    "Developer, data scientist, reader, mountain biker.",
                                                    className='card-text'
                                                ),
                                            ]
                                        ),
                                    ]
                                ), # end of me card

                                html.Br(),

                                # social
                                dbc.Card(
                                    [
                                        dbc.CardBody(
                                            [
                                                html.H4('Connect',className='card-title'),
                                                html.A(
                                                    'GitHub',
                                                    href='https://github.com/russellromney',
                                                    className='card-link',
                                                    target='_blank'
                                                ),
                                                html.A(
                                                    'LinkedIn',
                                                    href='https://linkedin.com/in/russellromney',
                                                    className='card-link',
                                                    target='_blank'
                                                ),
                                                
                                            ]
                                        )
                                    ]
                                ), # end social card

                                html.Br(),

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
    return 'This is the blog of '+name, 'Change name to {}case'.format(case)

