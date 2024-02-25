import pandas as pd
from config.config import Config

df = pd.read_csv(Config.PROCESSED_DATA_FILE)

df.rename(columns={
    'RegionName': 'region',
    'State':'state', 
    'Metro': 'metro',
    'CountyName': 'county'
    }, inplace=True)

df = df.astype({
    'region': str,
    'state': str,
    'metro': str,
    'county': str,
    'timestamp': 'datetime64[ns]'
})

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month

df = df.astype({
    'year': int,
    'month': int
})

df = df[['region', 'state', 'metro', 'county', 'year', 'month', 'timestamp', 'median_price']]

df.to_csv(Config.PROCESSED_DATA_FILE)