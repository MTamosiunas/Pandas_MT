#Section 10: Deleting

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', sep = ',')

wine = pd.DataFrame(df)

wine.drop(wine.columns[[0, 3, 6, 8, 10, 12, 13]], axis=1, inplace=True)

column_names = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
wine.columns = column_names

wine.at[0, 'alcohol'] = 'NaN'
wine.at[1, 'alcohol'] = 'NaN'
wine.at[2, 'alcohol'] = 'NaN'

wine.at[2, 'magnesium'] = 'NaN'
wine.at[3, 'magnesium'] = 'NaN'
print(wine)
print(wine.isnull().sum())
#wine.fillna({'alcohol' : 10, 'magnesium' : '100'}, inplace=True)
wine.at[0, 'alcohol'] = 10
wine.at[1, 'alcohol'] = 10
wine.at[2, 'alcohol'] = 10

wine.at[2, 'hue'] = '100'
wine.at[3, 'hue'] = '100'
print(wine)

print(wine.isnull().sum())


print(np.random.randint(0, 10, 10))