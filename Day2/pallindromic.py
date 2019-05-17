# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:08:47 2019

@author: User
"""
n=int(input("enter length : "))
list1=[]
list2=[]
list1.append(input(i).split()) 
for i in range(n):
    list2.append(list1[0][i])
for x in list2:
    if x==x[::-1]:
        check=True
        break
    else:
        check=False
print(check)

    