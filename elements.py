import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_blog_utilities import (
    color_map,
    color_pairs
)

from settings import (
    theme_color,
    config_homepage
)

color = color_map[theme_color]
color2 = color_pairs[color]

###################
# STATIC

blog_navbar = \
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
    color=color2,
) # end navbar


blog_title = \
dbc.Row(dbc.Col(dbc.Card(
    [
        html.H2('Blog Title',className='card-title'),
        dbc.CardBody(
            html.H5('This is my Blog Title Section',className='card-subtitle')
        )
    ],
    style=dict(textAlign='center')
)))

main_content = \
dbc.Row(dbc.Col(
    dbc.Card(
        [
            dbc.Container(fluid=True,id='main-content')
        ],
    ),
))

next_previous_post = \
dbc.Row(
    [
        dbc.Col(
            [
                dbc.Button(
                    text,
                    id=which+'-button',
                    size='lg',
                    color='primary',
                    block=True,
                    outline=True
                )
            ],
            width=6
        )
        for text,which in zip(['<< Previous','Next >>'],['previous','next'])
    ]
)

x = dbc.CardDeck(
    [
        # previous
        dbc.Card(
            [
                '<< Previous'
            ],
            body=True,
            id='previous-post',
            inverse=True,
            color='success',
            style=dict(textAlign='center',cursor='pointer')
        ),

        # next
        dbc.Card(
            [
                'Next >>'
            ],
            body=True,
            id='next-post',
            inverse=True,
            color='success',
            style=dict(textAlign='center')
        ),
    ]
)


recommended_articles = \
dbc.Row(
    [
        dbc.Col(
            dbc.CardGroup(
                [
                    html.A(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5('Article 1',className='card-title'),
                                        html.H6('A sampling of the content of article 1.',className='card-subtitle'),
                                    ],
                                ),
                                dbc.CardImg(
                                    src='https://picsum.photos/200/200',
                                    bottom=True,
                                    #style=dict(height='100px',width='100px')
                                )
                            ],
                            style=dict(maxWidth='200px')
                        ),
                        href='/article-1'
                    )
                    for i in range(4)
                ],
            )
        )
    ],
)



###################
# DYNAMIC

#title
def Title(id=None):
    '''
    a title
    '''
    pass

# subtitle
def Subtitle(id=None):
    '''
    the subtitle of a post
    '''
    pass

# body
def Body(id=None):
    '''
    the body of a post
    '''
    pass

# section title
def SectionTitle(id=None):
    '''
    a section title within a post
    '''

def Post():
    '''
    a post object - the content of a given post
    '''