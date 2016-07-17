# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 00:18:11 2016

@author: Katie
"""

import pandas as pd
input_dataframe = pd.read_csv(r'C:\Users\Katie\Documents\Thinkful\data\lecz-urban-rural-population-land-area-estimates_continent-90m.csv')
input_dataframe['Continent']
print (input_dataframe[0:10])