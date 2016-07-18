# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 07:42:42 2016

@author: Katie
"""

import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data=data.split('\n')
data=[i.split(',') for i in data]

column_names = data[0] #first row of data
data_rows= data[1:] #following rows of data
df = pd.DataFrame(data_rows,columns=column_names)

#Alcochol data statistical functions
df['Alcohol'] = df['Alcohol'].astype(float)

print("The Alcohol Data mean is: ")
print('{}'.format(df['Alcohol'].mean()))

print("The Alcohol Data median is: ")
df['Alcohol'].median()

#course has stats.mode(df[Alcohol]) ... but that raises and undefined name error
print("The Alcohol Data mode is: ")
print('{}'.format(df['Alcohol'].mode()))

print("The Alcohol Data range is: ")
print('{}'.format(max(df['Alcohol'])-min(df['Alcohol'])))

print("The Alcohol Data std. deviation is: ")
print('{}'.format(df['Alcohol'].std()))

print("The Alcohol Data variance is: ")
print('{}'.format(df['Alcohol'].var()))


#Tobaco data statistical functions
df['Tobacco'] = df['Tobacco'].astype(float)

print("The Tobacco Data mean is: ")
print(df['Tobacco'].mean())

print("The Tobacco Data median is: ")
print(df['Tobacco'].median())

print("The Tobacco Data mode is: ")
print('{}'.format(df['Tobacco'].mode()))

print("The Tobacco Data range is: ")
print('{}'.format(max(df['Tobacco'])-min(df['Tobacco'])))

#scipy.stats.mode(df['Tobacco'])
print("The Tobacco Data std. deviation is: ")
print(df['Tobacco'].std())

print("The Tobacco Data variance is: ")
print(df['Tobacco'].var())



print(data)
