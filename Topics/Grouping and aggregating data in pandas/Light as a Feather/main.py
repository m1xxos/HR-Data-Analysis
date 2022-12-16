import pandas as pd

penguin_sample = {'species': {0: 'Gentoo', 1: 'Gentoo', 2: 'Gentoo', 3: 'Adelie', 4: 'Gentoo', 5: 'Gentoo', 6: 'Gentoo', 7: 'Chinstrap', 8: 'Chinstrap', 9: 'Chinstrap', 10: 'Adelie', 11: 'Chinstrap', 12: 'Chinstrap', 13: 'Chinstrap', 14: 'Adelie', 15: 'Adelie', 16: 'Adelie', 17: 'Adelie', 18: 'Adelie', 19: 'Adelie', 20: 'Adelie'}, 'island': {0: 'Biscoe', 1: 'Biscoe', 2: 'Biscoe', 3: 'Biscoe', 4: 'Biscoe', 5: 'Biscoe', 6: 'Biscoe', 7: 'Dream', 8: 'Dream', 9: 'Dream', 10: 'Dream', 11: 'Dream', 12: 'Dream', 13: 'Dream', 14: 'Torgersen', 15: 'Torgersen', 16: 'Torgersen', 17: 'Torgersen', 18: 'Torgersen', 19: 'Torgersen', 20: 'Torgersen'}, 'body_mass_g': {0: 5650.0, 1: 5600.0, 2: 4400.0, 3: 2900.0, 4: 5350.0, 5: 5550.0, 6: 5100.0, 7: 3800.0, 8: 2700.0, 9: 3675.0, 10: 3950.0, 11: 4000.0, 12: 3600.0, 13: 3775.0, 14: 4200.0, 15: 4100.0, 16: 3150.0, 17: 3300.0, 18: 3700.0, 19: 3550.0, 20: 4250.0}}

df = pd.DataFrame(penguin_sample)

# your code here
print(df.groupby("island").agg({"body_mass_g": "min"}))
