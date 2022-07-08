from datetime import datetime
import plotly.express as px
import pandas as pd
import numpy as np
import mysql.connector

db = mysql.connector.connect(host="localhost",
							user="root",
							password="ashutosh",
							database="test")
mycursor = db.cursor(buffered=True)


'''
Channel :: 1345
+----------+
| Instance |
+----------+
|       61 |
|      145 |
|      154 |
|      158 |
|      191 |
|      201 |
|      217 |
|      222 |
+----------+
'''

# for i in [61, 145, 154, 158, 191, 201, 217, 222]:

#     data = pd.DataFrame()
#     value = []
#     dates = []

#     mycursor.execute(f"SELECT Ch1345, Date, Time FROM DG1_y WHERE Instance={i}")
#     for x in mycursor.fetchall():
#         ch, date, time = x
#         date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M:%S')
#         value.append(ch)
#         dates.append(date)
    
#     data['dates'] = dates
#     data['Ch1345'] = value
#     data['Ch1345'] = np.where(data['Ch1345']=='Off', 0, 1)
#     fig = px.line(data, x='dates', y='Ch1345', title='Instance::'+str(i))
#     fig.show()



'''
Channel :: 1780
+----------+
| Instance |
+----------+
|      145 |
|      158 |
|      165 |
|      191 |
|      192 |
|      194 |
|      195 |
|      201 |
|      213 |
|      214 |
|      216 |
|      217 |
|      218 |
|      220 |
|      222 |
+----------+
'''

for i in [145, 158, 165, 191, 192, 194, 195, 201, 213, 214, 216, 217, 218, 220, 222]:

    data = pd.DataFrame()
    value = []
    dates = []

    mycursor.execute(f"SELECT Ch1780, Date, Time FROM DG1_y WHERE Instance={i}")
    for x in mycursor.fetchall():
        ch, date, time = x
        date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M:%S')
        value.append(ch)
        dates.append(date)
    
    data['dates'] = dates
    data['Ch1780'] = value
    data['Ch1780'] = data['Ch1780'].map({'Off':0, 'On':1, '':2})
    fig = px.line(data, x='dates', y='Ch1780', title='Instance::'+str(i))
    fig.show()




'''
Channel :: 1817
+----------+
| Instance |
+----------+
|        3 |
|       60 |
|       61 |
|      129 |
|      131 |
|      145 |
|      158 |
|      159 |
|      165 |
|      191 |
|      192 |
|      194 |
|      195 |
|      201 |
|      213 |
|      214 |
|      216 |
|      217 |
|      218 |
|      220 |
|      222 |
+----------+
'''

# for i in [3, 60, 61, 129, 131, 145, 158, 159, 165, 191, 192, 194, 195, 201, 213, 214, 216, 217, 218, 220, 222]:

#     data = pd.DataFrame()
#     value = []
#     dates = []

#     mycursor.execute(f"SELECT Ch1817, Date, Time FROM DG1_y WHERE Instance={i}")
#     for x in mycursor.fetchall():
#         ch, date, time = x
#         date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M:%S')
#         value.append(ch)
#         dates.append(date)
    
#     data['dates'] = dates
#     data['Ch1817'] = value
#     data['Ch1817'] = np.where(data['Ch1817']=='Off', 0, 1)
#     fig = px.line(data, x='dates', y='Ch1817', title='Instance::'+str(i))
#     fig.show()





'''
Channel :: 327
+----------+
| Instance |
+----------+
|       37 |
|      165 |
|      191 |
|      223 |
+----------+
'''

# for i in [37, 165, 191, 223]:

#     data = pd.DataFrame()
#     value = []
#     dates = []

#     mycursor.execute(f"SELECT Ch327, Date, Time FROM DG1_y WHERE Instance={i}")
#     for x in mycursor.fetchall():
#         ch, date, time = x
#         date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M:%S')
#         value.append(ch)
#         dates.append(date)
    
#     data['dates'] = dates
#     data['Ch327'] = value
#     fig = px.line(data, x='dates', y='Ch327', title='Instance::'+str(i))
#     fig.show()