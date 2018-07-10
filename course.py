#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:54:45 2017

@author: faris
"""

import numpy as np
import pandas as pd
import seaborn as se
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

#Now using the cut finction we convert them into categories
myData['femaleemployrate']=pd.cut(myData.femaleemployrate,5, labels=["v.low", "low", "medium", "High", "v.High"])
myData['incomeperperson']=pd.cut(myData.incomeperperson,5, labels=["v.low", "low", "medium", "High", "v.High"])
myData['alcconsumption']=pd.cut(myData.alcconsumption,5, labels=["v.low", "low", "medium", "High", "v.High"])
myData['armedforcesrate']=pd.cut(myData.armedforcesrate,5, labels=["v.low", "low", "medium", "High", "v.High"])
myData['lifeexpectancy']=pd.cut(myData.lifeexpectancy,5, labels=["v.low", "low", "medium", "High", "v.High"])

# This is the distrbution for the wohle world
c1 = myData['femaleemployrate'].value_counts(sort = False)
p1 = myData['femaleemployrate'].value_counts(sort = False, normalize = True)

c2 = myData['incomeperperson'].value_counts(sort = False)
p2 = myData['incomeperperson'].value_counts(sort = False, normalize = True)

c3 = myData['alcconsumption'].value_counts(sort = False)
p3 = myData['alcconsumption'].value_counts(sort = False, normalize = True)

c4 = myData['armedforcesrate'].value_counts(sort = False)
p4 = myData['armedforcesrate'].value_counts(sort = False, normalize = True)

c5 = myData['femaleemployrate'].value_counts(sort = False)
p5 = myData['femaleemployrate'].value_counts(sort = False, normalize = True)

c6 = myData['lifeexpectancy'].value_counts(sort = False)
p6 = myData['lifeexpectancy'].value_counts(sort = False, normalize = True)

#se.distplot(p1);
#se.distplot(c1, kde= True, rug=True);

#globalStats = data.describe()
#developedStats = developed.describe()
#emergeStats = emerge.describe()
#poorStats = poor.describe()
#if this does not work try converting into float format using numpy then divide into categories

#myData["femaleemployrate"] = np.float16(myData.femaleemployrate)
#myData['femaleemployrate']=pd.cut(myData.femaleemployrate,4)


# We want to look at developed/poor/emerging countries
devlopedCountries = ['Canada', 'Australia', 'United Kingdom', 'United States', 'Singapore']

poorCountries = ['Yemen, Rep.', 'Afghanistan', 'Bangladesh', 'Benin', 'Bhutan', 'Zambia']
emergeCountries = ['China', 'Brazil', 'Peru', 'India', 'Malaysia', 'Turkey']

developed = myData.loc[myData['country'].isin(devlopedCountries)]

emerge = myData.loc[myData['country'].isin(emergeCountries)]

poor = myData.loc[myData['country'].isin(poorCountries)]

# now lets see the distribution of female employ rate for each category

cd1 = poor['femaleemployrate'].value_counts(sort = False, normalize = True)

cd2 = developed['femaleemployrate'].value_counts(sort = False, normalize = True)

cd3 = emerge['femaleemployrate'].value_counts(sort = False, normalize = True)

globalStats = data.describe()
developedStats = developed.describe()
emergeStats = emerge.describe()
poorStats = poor.describe()

names = devlopedCountries
values = developed['femaleemployrate']

#plt.figure(1, figsize=(6, 3))
#plt.scatter('country', 'femaleemployrate', data=emerge)
#plt.scatter('country', 'femaleemployrate', data=poor)
#plt.scatter('country', 'femaleemployrate', data=developed)

#plt.subplot(131)
plt.bar(names, values)
#plt.subplot(132)
#plt.scatter(names, values)
#plt.subplot(133)
#plt.plot(names, values)
plt.suptitle('Developed Countries female employ rate')
plt.show()