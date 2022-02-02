# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:48:54 2022

@author: Alberto Lucas
Bad Data Lab
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger


# 1
infile = 'https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv'
df = pd.read_csv(infile)

# 3
df.info()

# 4
df.isna().sum()        
df.isna().sum().sum()

# 5
# Some columns contain data with sentinel values (e.g. 'None')
df.apply(lambda x: x.value_counts().index[0])

# 6 and 7 
# Missing data is encoded in different ways within the same column (e.g. 'Retired' and 'None')
df['contbr_employer'].value_counts().head(n=20)

# 8
# Num values
len(df['memo_cd'].unique())
# Values count
df['memo_cd'].value_counts()
# Fraction of values empty
df['memo_cd'].isnull().mean()

# 9
# Seaborn
sns.distplot(df['contb_receipt_amt'])
plt.title('Histogram of contribution amounts')
plt.xlabel('Contribution amount (US dollars)')
plt.ylabel('Count')

# 10
df.describe()
# The min is suspicious because it is negative
df_neg = df[df['contb_receipt_amt'] < 0][['contbr_nm', 'contb_receipt_amt']]
df_neg['contb_receipt_amt'].value_counts()
# Checking if negative values correlate to positive values - They don't
temp = df[df['contb_receipt_amt'].abs() == 2700.0][['contbr_nm', 'contb_receipt_amt']]
temp['contb_receipt_amt'].value_counts()

# 11
df['contbr_zip'].str.len().value_counts()

# 12
# Shorter names seem to be popular, probably because they are easier
# to remember or represent acronyms. Additionally, there are the shorter
# sentinel values to consider.
df['contbr_employer'].str.len().hist()

# 13
contb_min = df['contb_receipt_amt'].min()
contb_max = df['contb_receipt_amt'].max()
df['s_amt1'] = (df['contb_receipt_amt'] - contb_min)/(contb_max - contb_min)

# 14
df_memo = df[['memo_cd', 'memo_text']]
# what memo_text values are associated with memo_cd values of X?
df[df.memo_cd == 'X'].memo_text.value_counts()
# how does this compare to the memo_text values when memo_cd is not X?
df[df.memo_cd.isnull()].memo_text.value_counts()
# X is used when the contribution is not earmarked.  However, X does not appear
# to be used for only earmarked contributions

# are any memo_text values shared between the two cases of memo_cd?
memo_x    = df[df.memo_cd == 'X'].memo_text.unique()
memo_notx = df[df.memo_cd.isnull()].memo_text.unique()
set(memo_x) & set(memo_notx)
# Only one non-NA value is in the intersection
df.groupby(['memo_cd', 'memo_text']).size().reset_index().rename(columns={0:'count'})

#16
df['s_amt2'] = (df['contb_receipt_amt'] - df['contb_receipt_amt'].mean()) / df['contb_receipt_amt'].std()
