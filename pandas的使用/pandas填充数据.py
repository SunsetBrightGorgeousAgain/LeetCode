import pandas as pd
df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})
print(df)
df1 = df.ffill()
# print(df1)

df2 = df.bfill()
print(df2)
