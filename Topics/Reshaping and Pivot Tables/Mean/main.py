#  write your code here
import pandas as pd

df = pd.read_csv("./data/dataset/input.txt")

df = df.pivot_table(index="labels", aggfunc="mean")
print(df.loc[["R"], ["null_deg"]].round(2).values)
