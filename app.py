import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__)

df = pd.read_pickle("./Data/dataset.pkl")
df['Date_data'] = df['Date'].str[:7]
date_values = list(df['Date_data'].unique())

categ_dict = {'TotalPlastic': 'Total Plastic',
    'SUM_Hard_PlasticBeverageBottle': 'Plastic Beverage Bottle',
    'SUM_Hard_OtherPlasticBottle': 'Other Plastic Bottle',
    'SUM_HardOrSoft_PlasticBottleCap': 'Plastic Bottle Cap',
    'SUM_PlasticOrFoamFoodContainer': 'Plastic Or Foam Food Container',
    'SUM_Hard_BucketOrCrate': 'Bucket Or Crate',
    'SUM_Hard_Lighter': 'Lighter',
    'SUM_OtherHardPlastic': 'Other Hard Plastic',
    'SUM_PlasticOrFoamPlatesBowlsCup': 'Plastic Or Foam Plates Bowls Cup',
    'SUM_HardSoft_PersonalCareProduc': 'Personal Care Produc',
    'SUM_HardSoftLollipopStick_EarBu': 'Lollipop Stick',
    'SUM_Soft_Bag': 'Bag',
    'SUM_Soft_WrapperOrLabel': 'Wrapper Or Label',
    'SUM_Soft_Straw': 'Straw',
    'SUM_Soft_OtherPlastic': 'Other Plastic',
    'SUM_Soft_CigaretteButts': 'Cigarette Butts',
    'SUM_Soft_StringRingRibbon': 'String Ring Ribbon',
    'SUM_FishingLineLureRope': 'Fishing Line Lure Rope',
    'SUM_Foam_OtherPlasticDebris': 'Foam Other Plastic Debris',
    'SUM_OtherPlasticDebris': 'Other Plastic Debris'}

app.layout = html.Div(children=[
    html.H1(children='TARS'),
    html.Div(children='''Leveraging AI/ML for plastic marine debris
    '''),
    html.Div(children=[
        dcc.Dropdown(
            id='demo-dropdown',
            options=[
                {'label': 'Total Plastic', 'value':'TotalPlastic'},
                {'label': 'Plastic Beverage Bottle', 'value': 'SUM_Hard_PlasticBeverageBottle'} ,
                {'label': 'Other Plastic Bottle', 'value': 'SUM_Hard_OtherPlasticBottle'} ,
                {'label': 'Plastic Bottle Cap', 'value': 'SUM_HardOrSoft_PlasticBottleCap'} ,
                {'label': 'Plastic Or Foam Food Container', 'value': 'SUM_PlasticOrFoamFoodContainer'} ,
                {'label': 'Bucket Or Crate', 'value': 'SUM_Hard_BucketOrCrate'} ,
                {'label': 'Lighter', 'value': 'SUM_Hard_Lighter'} ,
                {'label': 'Other Hard Plastic', 'value': 'SUM_OtherHardPlastic'} ,
                {'label': 'Plastic Or Foam Plates Bowls Cup', 'value': 'SUM_PlasticOrFoamPlatesBowlsCup'} ,
                {'label': 'Personal Care Produc', 'value': 'SUM_HardSoft_PersonalCareProduc'} ,
                {'label': 'Lollipop Stick', 'value': 'SUM_HardSoftLollipopStick_EarBu'} ,
                {'label': 'Bag', 'value': 'SUM_Soft_Bag'} ,
                {'label': 'Wrapper Or Label', 'value': 'SUM_Soft_WrapperOrLabel'} ,
                {'label': 'Straw', 'value': 'SUM_Soft_Straw'} ,
                {'label': 'Other Plastic', 'value': 'SUM_Soft_OtherPlastic'} ,
                {'label': 'Cigarette Butts', 'value': 'SUM_Soft_CigaretteButts'} ,
                {'label': 'String Ring Ribbon', 'value': 'SUM_Soft_StringRingRibbon'} ,
                {'label': 'Fishing Line Lure Rope', 'value': 'SUM_FishingLineLureRope'} ,
                {'label': 'Foam Other Plastic Debris', 'value': 'SUM_Foam_OtherPlasticDebris'} ,
                {'label': 'Other Plastic Debris', 'value': 'SUM_OtherPlasticDebris'} ,
            ],
            value='TotalPlastic', style={'width': '30%', 'display': 'inline-block'}
        ),
        html.Div(children=[
        dcc.Slider(
            id='year--slider',
            min=0,#df['Date_data'].min(),
            max=len(df['Date_data'].unique()),#df['Date_data'].max(),
            value=0,#df['Date_data'].max(),
            marks={str(year): i for i, year in zip(df['Date_data'].unique(), range(len(df)))},
            step=None
        )], style={'width': '68%', 'display': 'inline-block'})
    ]
    ),
    html.Div(
        children=[
            dcc.Graph(
            id='main-map', style={'width': '48%', 'display': 'inline-block'}
        ),
        dcc.Graph(
            id='qtd', style={'width': '48%', 'display': 'inline-block'}
        )
        ]
    )
])

@app.callback(
    Output('main-map', 'figure'),
    [Input('demo-dropdown', 'value'), Input('year--slider', 'value')]
    )
def update_figure(col, dt):
    fig = px.scatter_mapbox(df[df['Date_data']==date_values[dt]], lat="Lat", lon="Lon", hover_data=[col], size_max=30,
                            size=col, zoom=3, height=600)
    fig.update_layout(mapbox_style="open-street-map", title=categ_dict[col])
    return fig


@app.callback(
    Output('qtd', 'figure'),
    Input('year--slider', 'value')
    )
def update_figure(dt):
    aaa = pd.DataFrame(df[df['Date_data']==date_values[dt]].filter(regex='SUM_').sum()).reset_index()
    aaa['index'] = aaa['index'].map(categ_dict)
    aaa.columns = ['Type of plastic', '# Objects']

    fig = px.bar(aaa.sort_values('# Objects'), x='# Objects', y='Type of plastic', orientation='h', height=600)
    fig.update_layout(template='simple_white')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8080')