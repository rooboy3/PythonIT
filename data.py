import pandas as pd
import matplotlib.pyplot as plt  
import calendar

df = pd.read_csv("data.csv")
monthList = df['month_number'].apply(lambda x: calendar.month_abbr[x])
profitList = df ['total_profit'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.grid(True)
plt.show()