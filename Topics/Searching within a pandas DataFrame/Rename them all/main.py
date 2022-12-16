import pandas as pd

data = {"Product ID": {0: "TEC-AC-10004633", 1: "OFF-ST-10001418", 2: "OFF-ST-10001418", 3: "FUR-FU-10000409", 4: "TEC-PH-10003171", 5: "TEC-AC-10000682", 6: "OFF-FA-10004854", 7: "OFF-PA-10003673", 8: "OFF-ST-10001418", 9: "FUR-TA-10002228", 10: "OFF-ST-10003716", 11: "OFF-BI-10000977" , 12: "TEC-DE-2334553"}, "Segment": {0: "Corporate", 1: "Consumer", 2: "Home office", 3: "Consumer", 4: "Consumer", 5: "Consumer", 6: "Consumer", 7: "Corporate", 8: "Consumer", 9: "Consumer", 10: "Consumer", 11: "Corporate", 12: "Home office"}, "Destination city": {0: "Overland Park", 1: "Commerce City", 2: "Commerce City", 3: "Oceanside", 4: "Bloomington", 5: "Bloomington", 6: "Oceanside", 7: "Overland Park", 8: "Commerce City", 9: "Oceanside", 10: "Bloomington", 11: "Overland Park", 12: "Bloomington"}, "Quantity": {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 3, 6: 3, 7: 2, 8: 3, 9: 2, 10: 1, 11: 5, 12: 2}}

product_sales_by_city_and_segment = pd.DataFrame(data)

# your code here
print(
product_sales_by_city_and_segment.query("Segment != 'Corporate' & `Destination city` in ['Bloomington', 'Oceanside']")
)
