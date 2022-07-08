import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\Instances_1652.csv')
data1 = data[data['Instance']!=0]

# fig = px.line(data1, x='Instance', y='Ch 1657')
# fig.write_html(r'C:\Users\a\Desktop\APMS Nihal & Ashutosh\Malay & Dhruv\Instance\1652\1657_Inst.html')

for Ins, df in data.groupby('Instance'):
    print(Ins)
    print(df['Ch 1657'].value_counts())
    print('-'*15)