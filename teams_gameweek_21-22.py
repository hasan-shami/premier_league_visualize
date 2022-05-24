import pandas as pd

df = pd.read_excel(r'C:\Users\hasan.shami\Downloads\epl-2021-GMTStandardTime.xlsx')
df['Result_Home'] = df['Result'].apply(lambda x: str(x).split('-')[0]).astype(int)
df['Result_Away'] = df['Result'].apply(lambda x: str(x).split('-')[1]).astype(int)



def get_points_home(x):
    if x['Result_Home'] > x['Result_Away']:
        return 3
    elif x['Result_Home'] == x['Result_Away']:
        return 1
    else:
        return 0


def get_points_away(x):
    if x['Result_Home'] > x['Result_Away']:
        return 0
    elif x['Result_Home'] == x['Result_Away']:
        return 1
    else:
        return 3
df['Points Home'] = df.apply(lambda x: get_points_home(x), axis=1)
df['Points Away'] = df.apply(lambda x: get_points_away(x), axis=1)


df2 = df.pivot_table(index='Round Number', columns=['Home Team','Away Team'], values = ['Points Home', 'Points Away'], aggfunc = sum)

dfHome = df[['Round Number','Date','Home Team','Points Home']]
dfAway = df[['Round Number','Date','Away Team','Points Away']]

dfHome.rename(columns={"Home Team": 'Team',"Points Home": 'Points'},inplace = True)
dfAway.rename(columns={"Away Team": 'Team',"Points Away": 'Points'}, inplace= True)
df_master = dfHome.append(dfAway)
output = df_master.pivot_table(index='Round Number',columns = 'Team', values = 'Points', aggfunc=sum)
outputDate = df_master.pivot_table(index='Date',columns = 'Team', values = 'Points', aggfunc=sum)

import bar_chart_race as bcr