import matplotlib.pyplot as plt

# take age and prices as lists
age=[6,8,9,2,10,2,9,4,11,12,9]
price=[97,87,82,120,77,122,99,97,74,79,83]
plt.scatter(age,price,color='red')
plt.title('Age  and prices at Delhi')
plt.xlabel('Age in Years')
plt.ylabel('Price in lakhs of Rs')
plt.show()
