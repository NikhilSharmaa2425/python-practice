import pandas as pd
import matplotlib.pyplot as plt

x=[1001,1003,1006,1007,1009,1011]
y=[10000.00,23000.50,18000.33,16500.50,12000.75,9999.99]

x1=[1002,1004,1010,1008,1014,1015]
y1=[5000,6000,4500,12000,9000,10000]

df=pd.read_csv('D:\data\empdata.csv')

plt.bar(x,y,label='Sales data',color='red')
plt.bar(x1,y1,label='Production data',color='green')


plt.xlabel('emp ids')
plt.ylabel('salaries')

plt.title('TCS')

plt.legend()

plt.show()
