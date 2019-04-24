# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:06:51 2019

@author: sahil.agarwal
"""

def arrange(list1):
    for i in range(len(list1)):
        for j in range(0, len(list1)-i-1):
            if list1[j] > list1[j+1] :
                list1[j], list1[j+1] = list1[j+1], list1[j]
    file1 = open("WS2(01).txt", "w")
    file1.writelines(str(list1))
    file1.close()
    
list1 = []
for a in range(5):
    n = int(input('Enter a number: '))
    list1.append(n)
arrange(list1)