import pandas as pd
import matplotlib.pyplot as plt  
import calendar

df = pd.read_csv("data2.csv")
xList = df['Year'].tolist()
yList = df ['Total_Victoria','Regional_Victoria'].tolist()
plt.plot(xList, yList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(xList)
plt.title('')
plt.yticks([0, 20000, 40000, 60000])
plt.grid(True)
plt.show()