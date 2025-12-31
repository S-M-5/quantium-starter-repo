import pandas as pd
from dash import Dash, html, dcc
import plotly.express as plt

# Task 2 
csv0 = pd.read_csv('data/daily_sales_data_0.csv')
csv1 = pd.read_csv('data/daily_sales_data_1.csv')
csv2 = pd.read_csv('data/daily_sales_data_2.csv')
full_csv = pd.concat([csv0, csv1, csv2], ignore_index=True)
save_path = 'data/full_daily_sales_data.csv'
#full_csv.to_csv(save_path, index=False)

df = pd.DataFrame(full_csv)
df = df[df['product'] == 'pink morsel']
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = '$' + (df[['quantity', 'price']].prod(axis=1).astype(str))
df.drop(columns=['quantity', 'price','product'], inplace=True)
df = df[['sales', 'date', 'region']]
df.to_csv('data/pink_morsel_sales.csv', index=False)


# Task 3
app = Dash()
fig = plt.line(df, x = 'date', y = 'sales')
app.layout = html.Div(children = [
    html.H1(children = "Pink Morsel Sales", style={'textAlign': 'center', 'color': "#661160", 'font-size': 40}),
    html.Div(children = "A line chart of Pink Morsel sales from 2018-2022", style={'textAlign': 'center'}),
    dcc.Graph(
        id='graph',
        figure=fig
    )
])

app.run(debug=True)