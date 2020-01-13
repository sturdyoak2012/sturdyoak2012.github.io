#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 07:59:12 2020

@author: jacob
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.5,0.01,1.0)
y = x - 0.5

plt.plot(x,y)

plt.show()
