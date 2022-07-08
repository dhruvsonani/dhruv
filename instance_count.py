import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="ashutosh",
                                database="test")
mycursor = mydb.cursor(buffered=True)

df = pd.ExcelFile(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Documents\RCS Signals with Equipment Name_INS Sunayna_Segregated.xlsx')
df = df.parse('DG1')
df = df[df['Removed']=='No'][['Description']]

data = pd.DataFrame()
channels = []
zeros = []
ones = []
for ch in [324, 325, 326, 327, 329, 330, 331, 1345, 1654, 1655, 1656, 1657, 1773, 1778, 1780, 1817]:
    ch_name = str(ch) + '_label'
    mycursor.execute(f'SELECT {ch_name}, count(*) from dummy_2 GROUP BY {ch_name}')
    x = mycursor.fetchall()
    if len(x) == 2:
        channels.append(ch)
        zeros.append(x[0][1])
        ones.append(x[1][1])
    else:
        channels.append(ch)
        zeros.append(0)
        ones.append(x[0][1])        

data['Channel'] = channels
data['Description'] = df['Description'].values
data['0_count'] = zeros
data['1_count'] = ones
data = data.set_index('Channel')
print(data)