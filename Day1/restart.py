# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:05:10 2019

@author: Hitesh
"""

str1 = "RESTART"
print(str1)
loc=str1.find('R')
str2 = str1[loc+1:]
print(str1[:loc+1]+str2.replace('R','$'))
