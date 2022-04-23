import pandas as pd
from _tslabel_weak import tslabel_weak as ts

df = pd.read_excel('test_dataset\Cepea_milho.xls')
df.set_index('date', inplace=True)

df_tx = pd.read_excel('test_dataset\Scraping_Cepea_En_Noticias.xlsx', index_col='Date')
df_tx.index = pd.to_datetime(df_tx.index)

test = ts(txt=df_tx, col_txt='Text_Headline',serie=df, pct=0.03, col='real')