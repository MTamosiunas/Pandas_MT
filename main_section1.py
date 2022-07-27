#Section 1: Getting and knowing your data

import numpy as np
import pandas

import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep = '|')
#print(df)

users = pandas.DataFrame(df)
users = users.set_index('user_id')

print(users.head(25))
print(users.tail(10))

print(users)
print('--------------')

print(users.columns)
print('--------------')

print(users.info())
print('--------------')

print(users['occupation'].to_string(index=False))

print(users['occupation'].nunique())

print(users['occupation'].mode())

print(users.describe(include='all'))

print('***************')
print(users['age'].describe())
print('***************')
print(users['gender'].describe())
print('***************')
print(users['occupation'].describe())
print('****************')
print(users['zip_code'].describe())
print('***************')

print(users['age'].mean())

print(users['age'].value_counts().idxmin())

