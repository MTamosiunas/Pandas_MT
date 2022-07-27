#Section 2: FILTERING AND SORTING

import numpy as np
import pandas
#import pandas as pd

df=pandas.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep = ',')
#print(df)

euro12 = pandas.DataFrame(df)

print(euro12.iloc[:,[1]])

print(euro12['Team'].describe())

print(euro12.notnull().any().sum())

print(euro12.iloc[:,[0,  -5, -4]])

discipline = pandas.DataFrame(euro12[['Team', 'Yellow Cards', 'Red Cards']])
print(discipline)

print('-------------------------------------------------------')
discipline=discipline.sort_values(by=["Red Cards", "Yellow Cards"], ascending=[False, False])
print(discipline)

discipline_mean=discipline["Yellow Cards"].mean()
print(discipline_mean)

goal_filter = euro12[euro12['Goals']>6]
print(goal_filter)

name_filter = euro12[euro12['Team'].str.startswith('G')]
print(name_filter)

print(euro12.iloc[:,0:7])


print(euro12.loc[:, ~euro12.columns.isin (['Players Used', 'Subs off', 'Subs on'])])

print(euro12.iloc[[3, 7, 12], 4])


