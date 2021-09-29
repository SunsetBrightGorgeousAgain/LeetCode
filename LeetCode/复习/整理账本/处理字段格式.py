import pandas as pd

# df = pd.read_excel('1921.xls')
df = pd.read_excel('2018.xls')
df['日期'] = df['日期'].apply(lambda x: x[0:4] + '年' + x[5:7] + '月' + x[8:] + '日')
df['收入金额'] = df['收入金额'].fillna(0)
df['支出金额'] = df['支出金额'].fillna(0)
df['金额'] = df['收入金额'] + df['支出金额']
df.drop(columns='收入金额', inplace=True)
df.drop(columns='支出金额', inplace=True)
df.drop(columns='子类', inplace=True)
df.drop(columns='昵称', inplace=True)
df['备注2'] = df['备注']
df.drop(columns='备注', inplace=True)
df.rename(columns={'备注2': "备注"}, inplace=True)
print(df)
df.to_csv('1335new.csv', index=None, encoding='utf-16',sep='\t')
