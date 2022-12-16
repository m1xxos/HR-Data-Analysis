# your code here. the dataset is already loaded as sales_data.

print(sales_data.query("(Category == 'Technology' | Category == 'Furniture') & Sales < 25"))
