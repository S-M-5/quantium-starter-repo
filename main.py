import pandas as pd


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