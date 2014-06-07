# -*- coding: utf-8 -*-
"""
Created on Wed May 14 21:17:49 2014

@author: ozziegooen
"""

import numpy as np
from random import *
import matplotlib.pyplot as plt

mu, sigma = 1000., 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 1000)
b = np.random.lognormal(mu, sigma, 1000)
c = b * s
plt.hist(c, 1000, normed=True, align='mid')
#x = np.linspace(min(bins), max(bins), 10000)
#pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
#       / (x * sigma * np.sqrt(2 * np.pi)))
plt.axis('tight')
plt.show()