import pandas as pd

a_dict = dict()
a_dict['A'] = [1, 2, 3, 4]
a_dict['B'] = [2, 8, 10, 4]
df = pd.DataFrame(a_dict)
df['C'] = df['B'].cumsum()
df['D'] = df['B'].sum()
print(df)
