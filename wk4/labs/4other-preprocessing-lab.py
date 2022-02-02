# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:23:53 2022

@author: Alberto Lucas
Preprocessing Lab
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
sns.set()
sns.set_context('paper') 

# 1
wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")

# 2
df = wine.sample(20)
df.reset_index(inplace=True)

# 3
df = df.apply(zscore)

# 4
df.min()

# 5
df.max()

# 6
df = wine.sample(20)
df.reset_index(inplace=True)
df = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

# 7
df.apply(np.min, axis=0)
df.apply(np.max, axis=0)

# 8
df = wine
df.corr()

# 9
# most positively correlated
df.corr().apply(lambda x: x.sort_values(ascending=False).index[1])
# most negatively correlated
df.corr().apply(lambda x: x.sort_values().index[0])

# 10
# note that you get a kind of free heat map if you
# save the output of corr() as a dataframe and look
# at it with the Spyder variable explorer
# another way to plot
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)

# 11
# Most correlated to "Quality": volatile acidity is negatively correlated,
# whereas alcohol is somewhat positively correlated

# 12
# There are no nan values and all values seem valid. Therefore, the data is
# considered tidy.
df.isnull().sum().sum()


# 13
# Generate some fake GPA data using the following code:
n=10   # number of students
sem_years = np.array([s+' '+str(y) for y in np.arange(14,19) for s in ['spring', 'fall']])
gpa = np.random.normal(loc=3, scale=0.5, size=(n,sem_years.size))
gpa = np.clip(gpa, 0, 4)
gpa = pd.DataFrame(gpa, columns=sem_years)
otter_ids = pd.DataFrame({'otter_id': np.random.randint(1000, 10000, n)})
gpa_by_semester = pd.concat([otter_ids, gpa], axis=1)

# 14
gpa_by_semester_long = pd.melt(gpa_by_semester, id_vars=['otter_id'], var_name='semester', value_name='gpa')

# 15
gpa_by_semester_long['semester'] = pd.Categorical(gpa_by_semester_long['semester'], ordered=True, categories=sem_years)
gpa_by_semester_long.sort_values(['otter_id', 'semester'], inplace=True)
