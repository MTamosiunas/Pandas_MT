#Section 8: CREATING SERIES AND DATAFRAMES

import numpy as np
import pandas as pd


data = {'' : [0,1,2,3],
        'evolution' : ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
        'hp' : [45, 39, 44, 45],
        'name' : ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
        'pokedex' : ['yes', 'no', 'yes', 'no'],
        'type' : ['grass', 'fire', 'water', 'bug']}
#print(data)

pokemon = pd.DataFrame(data)
pokemon = pokemon.set_index('')
print(pokemon)

titles  = list(pokemon.columns)
titles[0], titles [1], titles [2], titles [3], titles [4] = titles [2], titles [4], titles [1], titles [0], titles [3]
print(titles)

pokemon = pokemon[titles]
#print(pokemon)

pokemon.insert(5, "place", ['LT', 'LV', 'EE', 'PL'])
#print(pokemon)

print('-------------------------------------------------')
print('Data type of each column of "pokemon" Dataframe :')
print(pokemon.dtypes)

ser = pd.Series(data)
print(ser)