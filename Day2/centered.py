# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:55:00 2019

@author: Mohit kumar
"""
list1=[1,2,3,100]
def ndu(list1):
    print('Non duplicate value : ',set(list1))
    Sum=0
    count=0
    for i in range(len(list1[1:-1])):
        count+=1
        Sum+=list1[i+1]
        print('{} :  ',Sum),''.format(i)
    print(count)
    print('Total sum: ',Sum)
    print('Average: ',Sum/count)
    return '\t'
print(ndu(list1))