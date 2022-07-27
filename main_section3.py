#Section 3: GROUPING

import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv', sep = ',')
print(df)

drinks = pd.DataFrame(df)
#print(drinks)

print(drinks.groupby('continent').beer_servings.mean())

print(drinks.groupby('continent').wine_servings.describe())

print(drinks.groupby('continent').total_litres_of_pure_alcohol.mean())

print(drinks.groupby('continent').total_litres_of_pure_alcohol.median())

print('-spirit servings---------------')
print(drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max']))