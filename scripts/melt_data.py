import pandas as pd
from config.config import Config

df = pd.read_csv(Config.RAW_DATA_FILE, index_col=0)
df.drop(columns=['SizeRank'], inplace=True)
df_long = pd.melt(df, id_vars=df.columns[:4], var_name='timestamp', value_name='median_price')
df_long.to_csv(Config.PROCESSED_DATA_FILE)