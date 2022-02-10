# -*- coding: utf-8 -*-
"""

Code related to KNN lecture 1 lab

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# read the data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)

# ---------- 3 ----------
# Describe data
df.info()
df.describe()

# ---------- 4 ----------
# Split data and scale it
X = df[['Outstate', 'F.Undergrad']].values
y = (df['Private'] == 'Yes').values.astype(int) # Private = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ---------- 5 ----------
# Check that data is scaled
print(X_train[:10,:])

# ---------- 6 ----------
# Build kNN classifier and train it
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# ---------- 7 ----------
# Make predictions
predictions = clf.predict(X_test)

# ---------- 8 ----------
# compare first ten predictions with first ten correct values
print(predictions[:10])
print(y_test[:10])

# ---------- 10 ----------
# compute accuracy
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))

# ---------- 11 ----------
# try with k = 7 instead of the default value of 5
clf = KNeighborsClassifier(n_neighbors=7)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))

# ---------- 12 ----------
# alternative distance formula
clf = KNeighborsClassifier(metric='chebyshev')
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))
