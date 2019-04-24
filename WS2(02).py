# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:28:15 2019

@author: sahil.agarwal
"""

file1 = open("WS2(02.1).txt", "r")
file2 = open("WS2(02.2).txt", "w")
for a in file1:
    b = a.split()
    c = 