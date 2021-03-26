import pandas as pd
df = pd.read_excel("全部数据(1).xlsx")
need_df = df[['code','name','mktcap']]
need_df = need_df[need_df['mktcap']>=9000000]
need_df.to_excel("900.xlsx")
print(need_df)