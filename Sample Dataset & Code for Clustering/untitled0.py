#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:44:45 2017
for 3rd dataset data cleaning
@author: michelle
"""
import re

f= open('./Mapping_529.txt','r')
data=[]
max_num=0

for line in f.readlines():
    data.append(re.split(',|\r\n', line)[:-1])
    max_num += 1
    

GTAdict = dict()
for i in range(max_num):
    name = data[i][1]
    data[i][1] = int(name[8:10])
    
    key = data[i][1]
    GTAdict.setdefault(key, [])
    GTAdict[key].append(data[i][0])
        
g = open('./gold_landmark.csv','w')
for k,v in GTAdict.iteritems():
    g.write('Cluster '+str(k))
    for m,n in enumerate(v):
        g.write(','+n)
    g.write('\n')