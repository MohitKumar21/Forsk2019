# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:58:30 2019

@author: Mohit kumar
"""
import random as ra
count=0
n=ra.randint(1,11)
g=int(input("Guess any no.: "))
while g!=n:
    count+=1
    if g > n+3:
        print("Too HIGH!")
    elif g < n-3:
        print("Too LOW")
    elif g > n:
        print("You are closer to guess but stil high")
    elif g < n:
        print("You are closer to guess but still low")
    g=int(input("Try again: "))
print('You rock! you guess no. in ',count,'tries')
while g==n:
    count=1
    choice=int(input('Do you want to play again \n1. Yes\n2. No\n'))
while choice:
    if  choice==1:
        g=int(input("Guess any no.: "))
    elif choice==2:
        break
    else:
        print('wrong choice')











'''if n==m:
        print('Yes, it is match with random value')
    else:
        print('No, it\'s not match with random value {}'.format(m))
    print('\nYou want to paly again : \n1. Yes\n2. No ')
  '''  