# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:56:22 2019

@author: User
"""
def vowels(s):
    s ='mohit achara kumar'
    v=('a','e','i','o','u','A','E','I','O','U')
    for i in s:
        if i in v:
            s=s.replace(i,"")
    print(s)
    return s
print(vowels(s))