# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:20:06 2019

@author: Hitesh
"""

n=0
while n<10:
    print(n)
    n+=1

n=1
while True:
    print(n)
    n+=1    
    if n==10:
        break
    
n=0
while n<10:
    if n%2==0:
        print(n)
    n+=1
    
n=0
while True:
    if n==10:
        break
    elif n%2!=0:
        print(n)
    n+=1
        
n=0
while n<10:
    if n%2!=0:
        print(n)
    n+=1
    
n=0
while True:
    if n==10:
        break
    elif n%2!=0:
        print(n)
    n+=1        