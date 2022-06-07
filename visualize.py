import bar_chart_race as bcr
import pandas as pd

df2 = pd.read_excel('Output2.xlsx', index_col='Date')
df2 = df2.fillna('0')
df2 = df2.apply(pd.to_numeric)
df2.reset_index(inplace=True)
df2['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')
df2.set_index('Date', inplace=True)
df2 = df2.groupby('Date').sum()
df3 = df2.copy()

for i in df2.columns:
    max = 0
    index = 0
    for j in df3[i]:
        max = max + int(j)
        df3[i].iloc[index] = max
        index = index + 1

# df3.apply(pd.to_numeric)


x2 = pd.date_range(start='2021-08-12', end='2022-05-22', freq='D')

df3.index = pd.DatetimeIndex(df3.index)
df4 = df3.reindex(x2, method='ffill')
df4.reset_index(inplace=True)
df4['index'] = df4['index'].dt.strftime('%B %d')
df4.set_index('index', inplace=True)
#
df4.to_excel("Points_By_Date.xlsx")
bcr.bar_chart_race(df=df4, n_bars=20,
                   filename="PL_Viz.mp4", period_length=80,
                   fixed_max=True, steps_per_period=10,
                   title = "English Premier League 2021-22",
                   )
