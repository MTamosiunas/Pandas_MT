# Section 4: APPLY

import numpy as np
import pandas as pd
from datetime import datetime

df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv', sep = ',')

crime = pd.DataFrame(df)
print(crime.dtypes)

crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')

crime = crime.set_index('Year')

crime.drop('Total', axis=1, inplace=True)

area_normalized_data = {'Decade': ['C20_7th_decade', 'C20_8th_decade', 'C20_9th_decade', 'C20_10th_decade', 'C21_1st_decade'],
                 'Violent': [0.06971, 0.16199, 0.23729, 0.2955, 0.2355],
                 'Property': [0.09536, 0.19296, 0.24715, 0.25138, 0.21315],
                 'Murder': [0.12072, 0.21855, 0.2347, 0.24064, 0.18539],
                 'Forcible_Rape': [0.06616, 0.15498, 0.24192, 0.27914, 0.25781],
                 'Robbery': [0.07722, 0.1966, 0.25446, 0.27175, 0.19997],
                 'Aggravated_assault': [0.06405, 0.13953, 0.22608, 0.31361, 0.25673],
                 'Burglary': [0.10813, 0.23123, 0.26846, 0.21713, 0.17505],
                 'Larceny_Theft': [0.08927, 0.17874, 0.24224, 0.2612, 0.22855],
                 'Vehicle_Theft' : [0.09984, 0.18376, 0.22518, 0.27591, 0.21532]}
cheating = pd.DataFrame(area_normalized_data)
print(cheating)
