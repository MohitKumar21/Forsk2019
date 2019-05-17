# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:38:33 2019

@author: User
"""

def leapyear(year):
    if year%4==0:
        print("leap year")
    elif year%400==0 or year%4==0:
        print("leap year")
    else:
        print("Ordinary year")
leapyear(2016)
