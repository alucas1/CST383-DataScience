# -*- coding: utf-8 -*-
"""
Probability lab #6

@author: Alberto Lucas
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 1
# I originally learned this rule in statistics as the "Empirical Rule".
# This rule states that almost all the data in a normal distribution falls within
# three standard deviations of the mean. 68% of the data is within 1 SD of the mean, 
# 95% is within 2 SDs of the mean, and 99.7% of the data is within 3 SDs of the mean.
 
# 2
# Data sets that are normally distributed have a bell shaped distribution.
# For example, standardized tests are designed so that scores are normally
# distributed, thus creating a bell shaped graph. Additionally, the weight of 
# humans is normally distributed, with many people falling near the mean and fewer
# humans at the extremities of the distribution.

# 3
# Income is not normally distributed due to the extreme wealth of few individuals.
# I predict that income inequality would result in a right-skewed graph. The deaths
# of humans, on the other hand, should be left skewed as younger people are less
# likely to die than older people (ignoring wars and disasters).

# 4
# CDF stands for "Cumulative Distribution Function". A CDF describes data as an
# accumulation of values for each subsequent plot on a graph. In terms of probabilities,
# each plot on the graph describes a cumilation of probabilities up until that
# point on the graph; Each plot on the graph describes the proportion of values
# less than or equal to the current plot.

# 5
# The max value a CDF can take is the cumulitive value of all the probabilities.
# This value would be equal to 100%, or the value 1.

# 6
def norm_plot(mean, sd):
    x = np.linspace(mean - 3*sd, mean + 3*sd)
    probs = norm.pdf(x, loc=mean, scale=sd)
    plt.plot(x, probs, color="darkgreen")
    plt.title('PDF of normal dist. with mean {} and SD {}'.format(mean, sd))
    
norm_plot(5, 0.5)

# 7
x = np.random.normal(5, 0.5, size=1000)
sns.distplot(x)

# 8
# -- part a --------------
norm_plot(10, np.sqrt(0.04))
# -- part b --------------
# Per the empirical rule, 68% of data falls within 1 SD of the mean.
# 1 SD is equal to sqrt(0.04) = 0.2.  Therefore, 10 - 0.2 = 9.8 and 10 + 0.2 = 10.2
# Thus, 68% of the data falls within [9.8, 10.2]
# -- part c --------------
# Analytical solution: 1 SD = 0.2, so 2 SDs = 0.4. Per the empirical rule, 95%
# of the data in a normal distribution lies within 2 SDs of the mean.
#
# Simulation solution:
x = np.random.normal(10, 0.2, size=1000)
p = np.mean(np.absolute(x - 10.0) < 0.4)

# 9
# sample and plot histogram
x = np.random.normal(5, 0.5, size=1000)
plt.hist(x, bins=30, density=True)
# plot pdf of normal distribution
x = np.linspace(3, 7)
probs = norm.pdf(x, loc=5, scale=0.5)
plt.plot(x, probs)
