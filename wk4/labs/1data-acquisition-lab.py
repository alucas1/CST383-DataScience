# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:02:48 2022

@author: Alberto Lucas
Data acquisition examples and lab solutions
"""

import pandas as pd
import seaborn as sns
from matplotlib import rcParams

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 9,7

# 5 - Read data from excel file
df = pd.read_excel("D:\\Workspace\\Unemployment.xlsx", header=7)
df.head()

# 6 - Read CSV data from a URL
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/unemployment.csv")
df.head()

# 7
# Automating the data loading step allows others to precisely replicate the steps taken
# to analyze data, thus allowing them to easily replicate the study. Automation
# also allows data to be analyzed easily in case the data set is updated. Documentation
# can be provided in the code or on an accompanying document.

#8
# The documentation is provided on the site from which the data was obtained
# https://www.ers.usda.gov/data-products/county-level-data-sets/documentation/