import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Instances_1652_1.csv', parse_dates=['Date'])

temp = data[data['Instance']!=0]            
temp = temp.groupby('Instance').apply(lambda df: [df['Date'].min(), df['Date'].max(), (df['Date'][df['Date'].idxmax()] - df['Date'][df['Date'].idxmin()]).total_seconds()/60.0]).to_frame()
temp = temp[0].apply(pd.Series)
temp.columns = ['min','max','Duration']
temp = temp.reset_index()
print(temp)

temp.to_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Duration_1.csv', index=False)
