# -*- coding: utf-8 -*-
"""

Code related to KNN lecture 1 lab

"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

# set plot styles
sns.set()
sns.set_context('talk')
rcParams['figure.figsize'] = 8,6

# ---------- 2 ----------
# Load data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# ---------- 3 ----------
# Create a 2D NumPy array X from the 'Top10perc' and 'F.Undergrad' columns of df. 
predictors = ['Top10perc', 'F.Undergrad']
X = df[predictors].values

# ---------- 4 ----------
# Create a 1D NumPy array y from the 'Outstate' column of df.
target = 'Outstate'
y = df[target].values

# ---------- 5 ----------
# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# ---------- 6 ----------
# scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---------- 7 ----------
# build a kNN regressor and train it
regr = KNeighborsRegressor()
regr.fit(X_train, y_train)

# ---------- 8 ----------
# make predictions
predictions = regr.predict(X_test)

# ---------- 9 ----------
# compare first ten predictions with first ten correct values
print(predictions[:10].astype(int))
print(y_test[:10])

# ---------- 11 ----------
# compute Mean Squared Error of predictions
mse = ((predictions - y_test)**2).mean()
print('MSE: {0:.0f}'.format(mse))

# ---------- 12 ----------
# What MSE would you get if you always just used the average value of y_train as your prediction?
#  This is called a "blind prediction" because, when predicting tuition, it doesn't look at the values for Top10perc and F.Undergrad.
mse_blind = ((y_train.mean() - y_test)**2).mean()
print('blind MSE: {0:.0f}'.format(mse_blind))

# ---------- 13 ----------
# use k=7
regr = KNeighborsRegressor(n_neighbors=7)
regr.fit(X_train, y_train)
predictions = regr.predict(X_test)
mse = ((predictions - y_test)**2).mean()
print('MSE: {0:.0f}'.format(mse))

# ---------- 14 ----------
# using an alternative distance function
regr = KNeighborsRegressor(metric='chebyshev')
regr.fit(X_train, y_train)
predictions = regr.predict(X_test)
mse = ((predictions - y_test)**2).mean()
print('MSE: {0:.0f}'.format(mse))
