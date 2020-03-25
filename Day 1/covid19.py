# Task: 
# - Processed the data: On a particular date, If 70% number of confirmed case is zero, then Delete the column. i.e. whole February will be deleted and few more.
# - Plot the graph
#     - Country Wise
#     - Date Wise
#     - Continent Wise

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../Datasets/time_series_2019-ncov-Confirmed.csv')
# print(data.head())
# print(data.describe())
calcuation = (len(data)*70)/100
totalZeroCasesInCol = (data == 0).sum()
dropCol = [k for k,v in totalZeroCasesInCol.iteritems() if v > calcuation]
data.drop(dropCol, axis=1, inplace=True)
# print(data.info)

# Country wise ploting.
curData = data.groupby(data['Country/Region']).sum()
curData.drop(['Lat', 'Long'],axis=1, inplace=True)
# print(curData)

xCountry = curData.index[5:20]
yCountry = curData.iloc[5:20,-1]

plt.title('Country wise ploting',fontsize=16, fontweight='bold')
plt.xlabel('Countries')
plt.xticks(rotation=90)
plt.ylabel('NO. of confirmed cases')
plt.bar(xCountry, yCountry, color='red')
plt.show()

# Date Wise Ploting.

curData.loc['total'] = curData.sum(axis=0)
print(curData)

xDate = curData.columns
yDate = curData.loc['total']

plt.title('Date wise ploting')
plt.xlabel('Date',fontsize=16)
plt.xticks(rotation=90)
plt.ylabel('NO. of confirmed cases')

plt.plot(xDate,yDate, color='red')
plt.show()