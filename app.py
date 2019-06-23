import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import no_update


from settings import (
    config_name,
    config_description,
    config_github,
    config_linkedin,
    server_secret_key,
    theme_color
)

from elements import (
    blog_title,
    main_content,
    next_previous_post,
    recommended_articles,
    blog_navbar
)

from posts import (
    home,
    post_template
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
        blog_navbar,

        # TODO
        # location manager
        dcc.Location(id='url'),

        # TODO
        # store for cookies
        dcc.Store(id='browser-store'),

        # body
        dbc.Container(
            dbc.Row(
                [                    
                    # content engine
                    dbc.Col(
                        [
                            # title div
                            blog_title,

                            html.Br(),

                            # TODO
                            # main content
                            main_content,

                            html.Br(),

                            # TODO
                            # previous and next posts
                            next_previous_post,

                            html.Br(),

                            # TODO
                            # recommended articles
                            recommended_articles,

                            html.Br(),

                            # TODO
                            # comments (commento)
                            dbc.Row(dbc.Col(
                                dbc.Card('comments')
                            )),

                            html.Br(),
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
                ],
            ),
            fluid=True
        ), # end body

    ],
    style=dict(width='100%'),
)



@app.callback(
    Output('main-content','children'),
    [Input('url','pathname')]
)
def router(url):
    if url=='/post-template':
        return post_template.content
    return home.content