import pandas as pd

race_sample = {'Lap_1': [98109, 100573, 101467, 104196, 105340],
               'Lap_2': [93006, 93774, 93725, 94485, 95808],
               'Lap_3': [92713, 92900, 93208, 95664, 95436],
               'Lap_4': [92803, 92582, 92933, 93900, 95810]}

df = pd.DataFrame(race_sample, index=['Vettel', 'Hamilton', 'Webber', 'Massa', 'Rosberg'])

# your code here
print(df.agg(min, axis="columns"))
