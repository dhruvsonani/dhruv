import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="ashutosh",
                                database="test")
mycursor = mydb.cursor(buffered=True)

data = pd.ExcelFile(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Documents\RCS Signals with Equipment Name_INS Sunayna_Segregated.xlsx')
data = data.parse('DG1')
data = data[data['Removed']=='No'][['ChNo', 'Min']]

data_min = []
for i, row in data.iterrows():
    data_min.append((row.values[0], row.values[1]))

# for ch,_ in data_min:
#     ch = str(ch) + '_label'
#     # mycursor.execute(f'ALTER TABLE Instances DROP COLUMN {ch}')
#     mycursor.execute(f'ALTER TABLE Instances ADD COLUMN {ch} INT(1) DEFAULT 1')

for i in range(1, 226):
    if i not in [10, 25, 43, 50, 51, 62, 65, 73, 82, 83, 110, 126, 130, 135, 137, 139, 143, 147, 149, 150, 161, 163, 164, 166, 173, 180, 181, 182, 184, 185, 186, 187, 188, 189, 193, 196, 197, 198, 199, 200, 202, 203, 207, 211, 215, 219, 221, 225]:
        for ch, min_value in data_min:
            print(i, ch)
            mycursor.execute(f'SELECT Ch{ch} from dg1_y WHERE Instance={i}')
            values = []
            for x in mycursor.fetchall():
                values.append(x[0])
            if min_value in values:
                mycursor.execute(f"UPDATE Instances SET {ch}_label=0 WHERE Instance={i}")
    else:
        for ch, min_value in data_min:
            mycursor.execute(f"UPDATE Instances SET {ch}_label=0 WHERE Instance={i}")

mydb.commit()
mycursor.close()


