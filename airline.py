import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

air_df = pd.read_csv('/home/grim-reaper/Downloads/airline.csv')
selected_columns = [
    'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 
    'TailNum','ActualElapsedTime','CRSElapsedTime','AirTime','ArrDelay', 'DepDelay','Origin', 'Dest', 'Distance',
    'TaxiIn', 'TaxiOut', 'Cancelled','Diverted'
]
air_sub_df = air_df[selected_columns].copy()
month_year_df = air_sub_df.groupby('Year')['Month'].value_counts().unstack().T

month_2005_df = air_sub_df[air_sub_df.Year == 2005]['Month'].value_counts().to_frame().reset_index().rename(columns={'index':'Month','Month':'count'})
month_2006_df = air_sub_df[air_sub_df.Year == 2006]['Month'].value_counts().to_frame().reset_index().rename(columns={'index':'Month','Month':'count'})
month_2007_df = air_sub_df[air_sub_df.Year == 2007]['Month'].value_counts().to_frame().reset_index().rename(columns={'index':'Month','Month':'count'})
month_2008_df = air_sub_df[air_sub_df.Year == 2008]['Month'].value_counts().to_frame().reset_index().rename(columns={'index':'Month','Month':'count'})

months =[month_2005_df, month_2006_df,month_2007_df,month_2008_df]

font1 = {'family':'Inconsolata','color':'blue','size':20}
font2 = {'family':'Inconsolata','color':'darkred','size':15}

plt.subplots(figsize = (12,6))
sns.lineplot(data = month_2005_df, x = 'Month', y='count', color = 'blue', label='2005')
sns.lineplot(data = month_2006_df, x = 'Month', y='count', color = '#ff9700', label='2006')
sns.lineplot(data = month_2007_df, x = 'Month', y='count', color = 'green', label='2007')
sns.lineplot(data = month_2008_df, x = 'Month', y='count', color = 'red', label='2008')
plt.title('Monthly Trendline of Flight Numbers', fontdict=font1)

Top_20_destinations = air_sub_df.Dest.value_counts().nlargest(20).to_frame().reset_index().rename(columns={'index':'Dest','Dest':'count'})

fig, ax = plt.subplots(figsize = (10,6))
sns.barplot(data = Top_20_destinations, y = 'Dest', x = 'count')
plt.title('Top 20 destinations from San Francisco International Airport',fontdict=font1)
plt.ylabel('Detinations', fontdict=font2)
plt.xlabel('Count', fontdict= font2)

plt.show()

plt.legend()