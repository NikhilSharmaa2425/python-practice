import matplotlib.pyplot as plt
import seaborn as sns
mpg=sns.load_dataset('mpg')
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.scatterplot(data=mpg,x='horsepower',y='acceleration',hue='origin')
plt.subplot(2,2,2)
sns.scatterplot(data=mpg,x='horsepower',y='acceleration',hue='origin')
plt.subplot(2,2,3)
sns.boxplot(data=mpg,x='horsepower',y='acceleration',hue='origin')
plt.subplot(2,2,4)
sns.lineplot(data=mpg,x='horsepower',y='acceleration',hue='origin')
plt.show()
