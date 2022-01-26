# -*- coding: utf-8 -*-
"""
Probability lab #4

@author: Alberto Lucas
"""

import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# 1
# You apply to 10 companies for a job, and each company offers
# jobs to 20% of (qualified) applicants.  Compute a sample of
# replies, using 0 for no offer, and 1 for offer.
x = np.random.choice([0,1], size=10, p=[.8, .2])

# 2 
# Repeat the experiment 10,000 times, and record in an array
# the number of offers for each experiment.
offers = [np.sum(np.random.choice([0,1], size=10, p=[.8, .2])) for i in range(10000)]

# 3
# Plot your vector from 2 as a bar plot, showing for each possible
# value 0-10, the fraction of experiments that resulted in that value.
# Use the bar() function of matplotlib for the bar plot.  It takes
# two arguments: an array of x locations for the bars, and the values
# for the bar heights.
counts = np.bincount(offers)
probs = counts/len(offers)
plt.bar(list(range(len(probs))), probs)

# 4
# using your data from problem 3, create another graph, but this time,
# for value i (from 0-10) show the fraction of experiments in which
# the number of offers was less than or equal to i. The value for 10 should
# be 1.0.  (Hint: consider using function numpy.cumsum()).
cdf = np.cumsum(probs)
plt.bar(list(range(len(probs))), cdf)

# 5
# Create another plot as in part 3, but this time get your array 
# of values from  a call to function numpy.random.binomial().
offers = np.random.binomial(10, p=0.2, size=10000)
probs = np.bincount(offers)/10000
plt.bar(np.arange(len(probs)), probs)

# 6
# create another plot as in part 3, but this time get your array
# of values from calls to function scipy.stats.binom().  This
# function will give you the PMF of the binomial distribution, so
# you don't have to simulate a bunch of trials.
probs = binom.pmf(np.arange(11), 10, 0.2)
plt.bar(np.arange(11), probs)

# 7
# If you have time, compute the probability of getting 2 job offers 
# after 8 applications, given the the probability of an offer in one
# application is 0.1.  Do this through simulation and through the
# use of scipy.stats.binom().
#a) simulation
offers = np.random.binomial(8, p=0.1, size=10000)
probs = np.bincount(offers)/10000
probs[2]
#b) scipy.stats.binom()
binom.pmf(2, 8, 0.1)

# 8
# Independent Bernoulli trials are performed, with a probability ½ of success, 
# until there has been at least one success.  Find the PMF of the number of 
# trials performed. 
# a) Simulation
def trial(n):
    trials = np.random.binomial(1, p=0.5, size=n)
    count = 0
    
    for i in trials:
        count += 1
        if i == 1:
            break
    
    return count

runs = [trial(50) for i in range(10000)]
probs = np.bincount(runs)/10000
plt.bar(np.arange(len(probs)), probs)

# 9
# Independent Bernoulli trials are performed, with a probability ½ of success, 
# until there has been at least one success and at least one failure.  
# Find the PMF of the number of trials performed.  
# a) Simulation
def trial2(n):
    trials = np.random.binomial(1, p=0.5, size=n)
    count = 0
    successflag = False
    falseflag = False
    
    for i in trials:
        count += 1
        
        if i == 1:
            successflag = True
        else:
            falseflag = True
        
        if successflag & falseflag:
            break
    
    return count

runs = [trial2(50) for i in range(10000)]
probs = np.bincount(runs)/10000
plt.bar(np.arange(len(probs)), probs)
