# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 17:15:09 2017

@author: Michelle
"""

import os
for f in os.listdir("C:/Users/Michelle/Downloads/allsports/AllSports"):
    for j in range(266, -1, -1):
        if f == str(j)+".JPG0":
            os.rename(f, str(j+1)+".JPG")