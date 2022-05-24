import bar_chart_race as bcr
import pandas as pd
df = pd.read_excel('Output2.xlsx',index_col='Date')

bcr.bar_chart_race(df=df, n_bars=6)