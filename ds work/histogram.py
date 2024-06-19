import matplotlib.pyplot as plt
emp_ages=[22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19]
bins=[0,10,20,30,40,50,60]
plt.hist(emp_ages,bins,histtype='bar',rwidth=0.8,color='black')
plt.xlabel('employee ages')
plt.ylabel('no of employees')
plt.title('Wipro')
plt.legend()
plt.show()
