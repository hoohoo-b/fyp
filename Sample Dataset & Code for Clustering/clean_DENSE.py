#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:22:26 2017

@author: michelle
"""

import pandas as pd

left = pd.read_csv("DENSE.csv", header=0)
left["index1"] = left["index1"].apply(lambda x: x+1)
left["index2"] = left["index2"].apply(lambda x: x+1)
right = pd.read_csv("probNew_AllSports.csv", header=0)

result = pd.merge(left, right, how='left', on=['index1', 'index2'])

result.to_csv("data_allSports_DENSE.csv", index=False)