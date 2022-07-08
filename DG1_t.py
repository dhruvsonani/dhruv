import csv
import mysql.connector
import os

mydb = mysql.connector.connect(host="localhost",
							user="root",
							password="ashutosh",
							database="test")
mycursor = mydb.cursor(buffered=True)


path = r"C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\DG1_t.csv"

file = open(path)
csv_data = csv.reader(file)

print(path)
for row in csv_data:
	mycursor.execute('INSERT INTO DG1_t VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',row)
	#done

	
mydb.commit()
mycursor.close()
print("Done")