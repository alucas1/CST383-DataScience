# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:21:16 2022

@author: Alberto Lucas
Missing Data Lab
"""

import numpy as np
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

# 1
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

# 2
df.head()

# 3
df.info()

# 4
df.isnull().sum().sum()
df.isnull().sum().sum() / df.size

# 5
np.sum(df.isnull().sum(axis=1) > 0)

# 6
df.isnull().sum() / df.shape[0]

# 7
df.isnull().sum(axis=1) / df.shape[1]

# 8
x = df.isnull().sum() / df.shape[0]
x.plot.bar(title="Fraction NA values per column")

# 9
# It depends on the importance of the data and the amount of NA values

# 10
df_cleanrows = df.dropna()
df_cleanrows.isnull().sum().sum()

# 11
df_cleancols = df.dropna(axis=1)

# 12
df_cleanrows.size
df_cleancols.size

# 13
col_meds = { c:df[c].median() for c in df.columns }
df_med = df.fillna(col_meds)

# 14
col_means = { c:df[c].mean() for c in df.columns }
df_mean = df.fillna(col_means)

