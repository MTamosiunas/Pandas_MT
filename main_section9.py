#Section 9: TIME SERIES

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv', sep = ',')

apple = pd.DataFrame(df)
print(apple.dtypes)

apple['Date'] = pd.to_datetime(apple['Date'], format='%Y/%m/%d')

apple = apple.set_index('Date')
print(apple)

print(apple.duplicated(subset=None, keep = 'first').sum())

#print(apple.loc[::-1].reset_index(drop=True))


apple_scatter = apple.plot(use_index=True, y='Adj Close')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.show()