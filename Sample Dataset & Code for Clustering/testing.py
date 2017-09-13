#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:33:38 2017

@author: michelle
"""
import re

f=open('./landmark_url.csv','r')
url_dict=dict()
for line in f.readlines():
    line = re.split(',|\r|\n', line)
    key = line[0]
    url_dict.setdefault(key, [])
    url_dict[key].append(line[1])
    
print url_dict[str(1)]