# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:03:21 2019

@author: User
"""

star=int(input("enter the no. : "))
for star in range(0,star):
    print("* "*star)
for i in range(0,star+1):
    print("* "*(star-i+1))