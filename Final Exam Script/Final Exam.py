#Alex Adams Final BIS497 Summer 1 2020
import pandas as pd
import pickle
import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


YT = pd.read_csv("us-states.csv")

#Remove all but Pennsylvania
YT['valid'] = YT['state'] == 'Pennsylvania'
YT = YT[YT.valid == True]
del YT['valid']

YT['adj_deaths'] = YT['deaths']

#Adjust 21 and 22 APR per prof instructions although 
#it looks like a correction was already made by NYT....
adj21 = -282
adj22 = -297
YT.loc[YT['date'] == '2020-04-21','adj_deaths'] = YT.loc[YT['date'] == '2020-04-21','adj_deaths']+adj21
YT.loc[YT['date'] == '2020-04-22','adj_deaths'] = YT.loc[YT['date'] == '2020-04-22','adj_deaths']+adj22


#Convert Date to Datetime for easier plotting
YT['fordat'] = pd.to_datetime(YT['date'],infer_datetime_format=True)
del YT['date']

#Make Chart and Adjust
fig, ax = plt.subplots(figsize=(15,7))
ax.bar(YT['fordat'],YT['adj_deaths'], width = .4, color=(37/255, 93/255, 122/255, 1), edgecolor =(0, 0, 0, 0))
plt.ylabel('Number of Deaths')
plt.grid(axis='y')
plt.xlabel('Date')
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.show()

