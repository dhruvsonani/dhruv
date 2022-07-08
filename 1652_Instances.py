import pandas as pd

channel_no = 'Ch 1652'
data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\DG1_t.csv', usecols=['Date', 'Time', channel_no])
data['Date'] = data['Date'] + ' ' + data['Time']
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y %H:%M:%S')
data.drop(['Time'], axis=1, inplace=True)

values = []
streak_of_zero = 0
prev = None
val_to_fill = 1

for i, x in enumerate(data[channel_no]):

    if str(x) != 'nan' and str(prev) == 'nan':
        if streak_of_zero < 7:
            val_to_fill = str(x)
            values[-streak_of_zero:] = [val_to_fill]*streak_of_zero
            val_to_fill = 'Off'
        else:
            values[-streak_of_zero:] = ['Off']*streak_of_zero
    
    if str(x) != 'nan':
        streak_of_zero = 0
        values.append(x)
    elif str(x) == 'nan':                                    
        streak_of_zero += 1
        values.append('nan')
   
    prev = x

if streak_of_zero < 7 and streak_of_zero > 0:
    values[-streak_of_zero:] = [val_to_fill]*streak_of_zero
else:
    values[-streak_of_zero:] = ['Off']*streak_of_zero

instances = []
cnt = 0
prev = None
for x in values:
    if prev == 'Off' and x != 'Off':
        cnt += 1
    if x == 'Off':
        instances.append(0)
    else:
        instances.append(cnt)
    prev = x

data['Instance'] = instances
data.to_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Instances_1652_1.csv', index=False)