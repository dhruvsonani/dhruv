import pandas as pd
import warnings
warnings.filterwarnings("ignore")

ch_number = 'Ch 1780'
instances = [145,158,165,195,201,217,218,222]

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Model\Dataset.csv')
data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %H:%M:%S')
data = data.drop('Time', axis=1)
data = data[data['Instance'].isin(instances)]

new_data = pd.DataFrame()
for instance, df in data.groupby('Instance'):

    time_to_on = df[df[ch_number]=='On']['Date'].min()
    df = df[df['Date']>=time_to_on]
    new_data = new_data.append(df, ignore_index=True)


instance_min_time = {}
for inst, df in new_data.groupby('Instance'):
    first_idx = df[df[ch_number]=='Off'].index[0]
    instance_min_time[inst] = df.loc[first_idx, 'Date']

ttf = []
for x, i in zip(new_data['Date'], new_data['Instance']):
    ttf.append((instance_min_time[i] - x).total_seconds()/60.0)

new_data['TTF'] = ttf
new_data = new_data[new_data['TTF']>=0]

new_data.to_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Model\1780_TTF.csv', index=False)

print('File created!!!')

# data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Model\327_TTF.csv', parse_dates=['Date'])

# for instance, df in data.groupby('Instance'):
#     print(instance)
#     for i, x in enumerate(df['Date'].diff()):
#         try:
#             print(x.total_seconds())
#         except:
#             pass
#     print('='*10)
