# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:28:47 2019

@author: User
"""
list1=[5,2,6,2,3]
def add(list1):
    Sum=0
    for i in range(len(list1)):
        Sum+=list1[i]
    print('Total sum: ',Sum)
    return '\t'
def mul(list1):
    mult=0
    for i in range(len(list1)):
        mult*=list1[i]
    print('Multiplication : ',mult)
    return '\t'
def sort(list1):
    print('sorted list : ',sorted(list1))
    return '\t'
def largest(list1):
    print('largest value : ',max(list1))
    return '\t'
def smallest(list1):
    print('Smallest value : ',min(list1))
    return '\t'
def ndupli(list1):
    print('non duplicate value : ',set(list1))
    return '\t'
print(add(list1))
print(mul(list1))
print(largest(list1))
print(smallest(list1))
print(sort(list1))
print(ndupli(list1))