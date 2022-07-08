import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Duration_1.csv')
data = data[data['Duration']<=60]

plt.hist(data['Duration'], bins=60)
plt.vlines(10, ymin=0, ymax=10, linestyles='dashed', colors='red')
plt.suptitle("We'll take only instances having duration more than 10 min")
plt.xlabel('Duration')
plt.ylabel('Count')
plt.show()