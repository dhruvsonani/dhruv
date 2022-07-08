import mysql.connector

mydb = mysql.connector.connect(host="localhost",
							user="root",
							password="ashutosh",
							database="test")
mycursor = mydb.cursor(buffered=True)

count_of_null = []
table_name = 'dg1_t'
ch_name = 'Ch281'
mycursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {ch_name}=''")
count_of_null.append(mycursor.fetchall()[0][0])   
print(count_of_null)