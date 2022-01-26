# -*- coding: utf-8 -*-
"""
Probability lab #5

@author: Alberto Lucas
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

# 1
x = np.array([1,4,15])
probs = np.array([0.7, 0.28, 0.02])
plt.bar(range(len(x)), probs, tick_label=x)
plt.title("PMF of random variable X")

# 2
ex = np.sum(x * probs)

# 3
samp = np.random.choice(x, size=500, p=probs)
samp.mean()

# 4
# To make a profit, I should pay < $2.12 per box

# 5
samp.var()
np.sqrt(samp.var())

# 6
var = np.sum(probs * np.square(x - ex)) / (sum(probs))

# 7
# E(cX)
# = P(X = x_1)*(c*x_1) + ... + P(X = x_n)*(c*x_n)
# = c*(P(X = x_1)*x_1 + ... + P(X = x_n)*x_n)
# = c*E(X)

# 8
num_trials = 1000
success_prob = 0.02
max_plot = 40  # very low probability of > 40 Yodas
probs = binom.pmf(np.arange(num_trials+1), num_trials, success_prob)
plt.bar(np.arange(max_plot+1), probs[:(max_plot+1)], color="darkred")
plt.title('Probability of number of Yodas in 1000 boxes')

# 9
# Assuming a 1% daily chance that an ant will find the boxes and
# alert the colony (a clean house).
num_trials = 1000
success_prob = 0.01
max_days = 30  # days in a month
probs = binom.pmf(np.arange(max_days+1), num_trials, success_prob)
plt.bar(np.arange(max_days+1), probs[:(max_days+1)], color="darkred")
plt.title('Probability of having an ant problem')