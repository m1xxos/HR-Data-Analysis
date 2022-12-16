# your code here. The DataFrame is already loaded as a_rains.
print(a_rains[~((((a_rains.Location == 'Perth') & (a_rains.RainToday == 'No'))
       | ((a_rains.Location == 'Sydney') & (a_rains.RainToday == 'Yes')))
       & ~((a_rains.MaxTemp > 10) & (a_rains.Rainfall >= .3)))])