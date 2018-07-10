#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:09:55 2018

@author: faris
"""

import numpy as np
import pandas as pd
import seaborn as se
import matplotlib as mpl
import matplotlib.pyplot as plt
# Loading my dataset from the file exist in my directory
data = pd.read_csv("gapMinder.csv", low_memory = False 
                   ) # index_col=0, parse_dates=True

##printing the first few records of my data
#print (data.head())
#
##Printing the column names in my dataset
#print(data.columns)

# I am interseted only in the following columns (for the whole project)
'''countries, females-employ-rate,  income per-person, 
 armed-force-rate, life-expectancy, Alcohol consumption '''

# Now I want to extract those columns into my sub-DataFrame (tabular view)
myColumns = ['country', 'incomeperperson', 'alcconsumption', 'armedforcesrate',
              'femaleemployrate', 'lifeexpectancy']
myData = data[myColumns]

#First we convert the objects into numeric 
myData["femaleemployrate"] = pd.to_numeric(myData["femaleemployrate"],errors='coerce')
myData["incomeperperson"] = pd.to_numeric(myData["incomeperperson"],errors='coerce')
myData["alcconsumption"] = pd.to_numeric(myData["alcconsumption"],errors='coerce')
myData["armedforcesrate"] = pd.to_numeric(myData["armedforcesrate"],errors='coerce')
myData["lifeexpectancy"] = pd.to_numeric(myData["lifeexpectancy"],errors='coerce')

myData.lifeexpectancy.hist()

# We want to look at developed/poor/emerging countries
devlopedCountries = ['Canada', 'Australia', 'United Kingdom', 'United States', 'Singapore']

poorCountries = ['Yemen, Rep.', 'Afghanistan', 'Bangladesh', 'Benin', 'Bhutan', 'Zambia']
emergeCountries = ['China', 'Brazil', 'Peru', 'India', 'Malaysia', 'Turkey']

developed = myData.loc[myData['country'].isin(devlopedCountries)]

emerge = myData.loc[myData['country'].isin(emergeCountries)]

poor = myData.loc[myData['country'].isin(poorCountries)]