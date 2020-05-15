# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:09:11 2020

@author: Beka-abramishvili
"""



#2) დავალება
string = "4,5,6,15"
arr=[]

s=string.split(',')
print(arr)
5




#4) დავალება
a, b, c, d = input("texti: "), input(
    "texti: "), input("texti: "), input("texti: ")
array = []
array.append(a)
array.append(b)
array.append(c)
array.append(d)
for i in sorted(array, key=len, reverse=True):
    print(i)