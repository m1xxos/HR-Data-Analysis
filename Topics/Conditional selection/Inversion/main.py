import pandas as pd

australia_dict = {'Date': {0: '2017-06-04', 1: '2017-06-10', 2: '2017-06-06', 3: '2017-06-09', 4: '2017-06-03', 5: '2017-06-08', 6: '2017-06-12', 7: '2017-06-01'}, 'Location': {0: 'Perth', 1: 'Sydney', 2: 'Canberra', 3: 'Melbourne', 4: 'Canberra', 5: 'Sydney', 6: 'Perth', 7: 'Melbourne'}, 'MinTemp': {0: 12.1, 1: 12.5, 2: -3.2, 3: 6.6, 4: -4.2, 5: 12.4, 6: 6.4, 7: 7.9}, 'MaxTemp': {0: 22.2, 1: 18.1, 2: 12.8, 3: 15.0, 4: 15.4, 5: 18.1, 6: 24.2, 7: 13.9}, 'Rainfall': {0: 0.0, 1: 38.8, 2: 0.2, 3: 1.8, 4: 0.0, 5: 61.0, 6: 0.0, 7: 0.4}, 'WindGustDir': {0: 'SSE', 1: 'SSE', 2: 'SSE', 3: 'S', 4: 'W', 5: 'SE', 6: 'NE', 7: 'SSW'}, 'WindGustSpeed': {0: 22.0, 1: 50.0, 2: 56.0, 3: 22.0, 4: 19.0, 5: 44.0, 6: 35.0, 7: 20.0}, 'RainToday': {0: 'No', 1: 'Yes', 2: 'No', 3: 'Yes', 4: 'No', 5: 'Yes', 6: 'No', 7: 'No'}}

a_rains = pd.DataFrame(australia_dict)

# your code here
print(a_rains[~((((a_rains.Location == 'Perth') & (a_rains.RainToday == 'No'))
       | ((a_rains.Location == 'Sydney') & (a_rains.RainToday == 'Yes')))
       & ~((a_rains.MaxTemp > 10) & (a_rains.Rainfall >= .3)))])
