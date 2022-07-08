import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host="localhost",
							user="root",
							password="ashutosh",
							database="test")
mycursor = mydb.cursor(buffered=True)

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\RPM_Instance1.csv')

mycursor.execute('CREATE TABLE instances(Instance INT(5),min VARCHAR(20),max VARCHAR(20),Duration FLOAT(5), Hist_select INT(1));')

for i, value in data.iterrows():
	v = list(value.values)
	mycursor.execute('INSERT INTO instances VALUES (%s,%s,%s,%s,%s)', v)

mydb.commit()
mycursor.close()