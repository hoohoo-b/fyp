#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:22:26 2017

@author: michelle
"""

import pandas as pd
import numpy as np

left = pd.read_csv("DENSE.csv", header=0)
right = pd.read_csv("data_allSports.csv", header=0)

result = pd.merge(left, right, how='left', on=['index1', 'index2'])

result.to_csv('data_allSports_DENSE.csv', index=False)