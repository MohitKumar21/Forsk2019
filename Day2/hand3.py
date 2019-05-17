# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:42:16 2019

@author: User
"""

def days_in_month(month):
    li1=[1,3,5,7,8,10,12]
    li2=[4,6,9,11]
    if month in li1:
        print("31 days")
    elif month in li2:
        print("30 days")
    else:
        print("May be 28 or 29 days")
days_in_month(2)