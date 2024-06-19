import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('D:\data\empdata.csv')

print(df)
x=df['empid']
y=df['sal']
plt.bar(x,y,label='Employee data',color='yellow')
plt.xlabel('Employee ids')
plt.ylabel('Employee Salaries')
plt.title('Infosys')
plt.legend()
plt.show()
