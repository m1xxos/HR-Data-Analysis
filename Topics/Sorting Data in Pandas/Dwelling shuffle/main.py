import pandas as pd

df = pd.DataFrame({
    "type_of_dwelling": ['Private house', 'Townhouse', 'Apartment', 'Townhouse'], 
    "walls_material": ['wood', 'concrete', 'blocks', 'bricks'], 
    "number_of_persons": [4, 8, 2, 3]},
    index=[41, 44, 42, 43])

# your code here
print(df.sort_index())
