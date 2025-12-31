import pandas as pd
from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as plt

# Task 2 
csv0 = pd.read_csv('data/daily_sales_data_0.csv')
csv1 = pd.read_csv('data/daily_sales_data_1.csv')
csv2 = pd.read_csv('data/daily_sales_data_2.csv')
full_csv = pd.concat([csv0, csv1, csv2], ignore_index=True)
save_path = 'data/full_daily_sales_data.csv'
full_csv.to_csv(save_path, index=False)

df = pd.DataFrame(full_csv)
df = df[df['product'] == 'pink morsel']
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = '$' + (df[['quantity', 'price']].prod(axis=1).astype(str))
df.drop(columns=['quantity', 'price','product'], inplace=True)
df = df[['sales', 'date', 'region']]
df.to_csv('data/pink_morsel_sales.csv', index=False)


# Task 3 and 4
app = Dash()
fig = plt.line(df, x = 'date', y = 'sales')
app.layout = html.Div(children = [
    html.H1(children = "Pink Morsel Sales", style={'textAlign': 'center', 'color': "#B012A5", 'font-size': 40, 'font-family': ' Georgia, serif'}),
    html.Div(children = "A line chart of Pink Morsel sales from 2018-2022", style={'textAlign': 'center', 'color': "#B012A5", 'font-size': 20, 'font-family': ' Georgia, serif'}),
    dcc.Graph(
        id='graph',
        figure=fig
    ),
    html.Div(children = 
    dcc.RadioItems(
        id='region-filter',
        options=[{'label': region, 'value': region} for region in df['region'].unique()]+[{'label': 'all', 'value': 'all'}],
        value='All',
        labelStyle={'display': 'inline-block', 'margin-right': '10px', 'font-family': 'Georgia, serif'}
    ) , style={'textAlign': 'center', 'margin-top': '20px'}
    )
])

@callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='region-filter', component_property='value')
)
def region_filter(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    fig = plt.line(filtered_df, x='date', y='sales')
    return fig

app.run(debug=True)