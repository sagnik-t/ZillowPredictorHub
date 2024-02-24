import pandas as pd

df = pd.read_csv('./data/raw/City_MedianRentalPrice_AllHomes.csv', index_col=0)
df.drop(columns=['SizeRank'], inplace=True)
df_long = pd.melt(df, id_vars=df.columns[:4], var_name='timestamp', value_name='median_price')
df_long.to_csv('./data/processed/median_price_all_homes.csv')