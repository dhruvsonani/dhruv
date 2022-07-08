import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\DG_1.csv', usecols=['Ch 1652'])
new_data = []
count = 0
for x in data['Ch 1652']:
    if str(x) == 'nan':
        count += 1
    else:
        if count > 0:
            new_data.append(count)
            count = 0
data = [a for a in new_data if a<101]
plt.hist(data, bins=100)
plt.show()