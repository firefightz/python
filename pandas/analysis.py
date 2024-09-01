import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

# print(poke.tail(5))

# print([(key, val['Speed']) for (key, val) in poke.iterrows()])

df = poke.loc[poke['Speed'] == 104]
print(df)


