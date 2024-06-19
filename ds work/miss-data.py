import pandas as pd,xlrd
df=pd.read_csv('D:\data\empdata1.csv')
print(df)
df1=df.fillna(0)
print(df1)
df1=df.fillna({'ename':'Missing name','sal':0.00,'doj':'00-00-00'})
print(df1)
