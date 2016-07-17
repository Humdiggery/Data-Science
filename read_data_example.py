# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:09:54 2016

@author: Katie
"""

with open(r'C:\Users\Katie\Documents\Thinkful\data\lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header= next(inputFile)
    for line in inputFile:
        #rstrip removes any trailing lines or leading spaces
        line = line.rstrip().split()
        if line[1] == 'Total National Population':
            print(line)