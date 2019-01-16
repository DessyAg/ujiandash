import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from dash.dependencies import Input, Output
# from kategory import dfToko

color_set=['#000000','#FCE63D',]

engine = create_engine("mysql+mysqlconnector://root:dessy@localhost/titanic?host=localhost?port=3306")
conn = engine.connect()

results = conn.execute("SELECT * from titanic1").fetchall()
dfPlot = pd.DataFrame(data=results, columns = results[0].keys())
# dfPlot.set_index('Nama', inplace=True)


def generate_table(dataframe, max_rows=30):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        #knapa ada str=> karena datanya boolean 
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )




print(dfPlot.head())

#app =sebuah objek 
app = dash.Dash(__name__) 


#html.Div (terluar)
app.title ='Dashboard Titanic'
app.layout = html.Div(children=[
    html.H1(children='Dashboard Titanic', className='titledashboard'),
    #tabs = untuk global sedangankan tab = untuk satu baris
    dcc.Tabs(id="tabs", value='tab-1', children=[
        
        dcc.Tab(label='Titanic', value='tab-1', children=[
            html.Div([
                html.H1('Titanic', className='h1'),
                #html.table di return dari atas
                generate_table(dfPlot)
            ])
        ]),


        #  dcc.Tab(label='Scatter Plot', value='tab-2',children=[
        #     html.Div([
        #         html.H1('Scatter Plot Pokemon', className='h1'),

        #         dcc.Graph(
        #             id='ScatterPlot',
        #             figure={
        #                 'data': [
        #                     #go itu objek kenudian memiliki method scatter
        #                     go.Scatter(
        #                         x=dfPlot[dfPlot['Palette'] == col]['X'],
        #                         y=dfPlot[dfPlot['Palette'] == col]['Y'],
        #                         mode='markers',
        #                         marker=dict(color=color_set[i], size=10, line={'width' :0.5, 'color':'white'}),
        #                         name=str(col)
        #                     ) for col, i in zip(dfPlot['Palette'].unique(),range(2))
        #                 ], 
        #                 'layout':go.Layout(
        #                         xaxis={'title' :' Attack'},
        #                         yaxis={'title': 'Defense'},
        #                         margin={'l' : 40, 'b':40, 't':10, 'r':10},
        #                         #fungsi untuk menangkap data yang di zoom
        #                         hovermode='closest'
        #                 )

        #             }
        #         )
        #     ])
        # ])

        
        
        
       #merubah untuk dari luar tab nya 
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '50px'
    })
], style={
    'maxWidth': '3000px',
    'margin': '0 auto'
})


if __name__ == '__main__':
     
    app.run_server(debug=True, port=1997)