import pandas as pd

penguins_dict = {'species': 
                 {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo', 
                  3: 'Adelie', 4: 'Gentoo', 5: 'Chinstrap'}, 
                 'island': 
                 {0: 'Dream', 1: 'Dream', 2: 'Biscoe', 3: 'Biscoe', 
                  4: 'Biscoe', 5: 'Dream'}, 
                 'body_mass_g': {0: 3500, 1: 3500, 2: 5100, 
                                 3: 3400, 4: 4950, 5: 3250}}
penguins_example = pd.DataFrame(penguins_dict)

# your code here
penguins_example.sort_values(['species', 'body_mass_g'], inplace=True)
print(penguins_example)
