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

print(data)
