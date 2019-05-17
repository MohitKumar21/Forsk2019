# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:47:51 2019

@author: Hitesh
"""

Assignmentmarks = 0.0
totalAM = 0.0
TestMarks = 0.0
totalTM = 0.0
for i in range(0,3):
    Assignmentmarks = float(input("Enter Assignment Marks "))
    totalAM +=  Assignmentmarks
for i in range(0,2):
    TestMarks = float(input("Enter Test Marks "))
    totalTM += TestMarks
WeightedScore = totalAM*.10 + totalTM*.35
print("Weighted Score is",WeightedScore)