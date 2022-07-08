import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="ashutosh",
                                database="test")
mycursor = mydb.cursor(buffered=True)

# mycursor.execute(f'ALTER TABLE dummy_inst_1657 ADD COLUMN 1817_label INT(1) DEFAULT 0')

for i in range(1, 226):
    if i not in [10, 25, 43, 50, 51, 62, 65, 73, 82, 83, 110, 126, 130, 135, 137, 139, 143, 147, 149, 150, 161, 163, 164, 166, 173, 180, 181, 182, 184, 185, 186, 187, 188, 189, 193, 196, 197, 198, 199, 200, 202, 203, 207, 211, 215, 219, 221, 225]:
        mycursor.execute(f'SELECT Ch1817 FROM dg1_y WHERE Instance={i}')
        values = []
        for x in mycursor.fetchall():
            values.append(x[0])
        if 'On' in values:
            mycursor.execute(f"UPDATE dummy_inst_1657 SET 1817_label=1 WHERE Instance={i}")

mydb.commit()
mycursor.close()


