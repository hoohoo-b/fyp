#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:20:38 2017
landmark dataset: create url csv file
@author: michelle
"""
import re

f= open('./Mapping_529.txt','r')
data=[]
max_num=0

for line in f.readlines():
    data.append(re.split(',|\r\n', line)[:-1])
    max_num += 1
    
g = open('./landmark_url.csv','a')
for i in range(max_num):
    g.write(data[i][0])
    g.write(',')
    g.write(data[i][2])
    g.write('\n')
    
f.close()
g.close()