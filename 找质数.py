#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:42:34 2018

@author: xiangyinyu
"""

# 输入一个正整数，按照从小到大的顺序输出它的所有质数的因子
#（如180的质数因子为2 2 3 3 5 ）
# 最后一个数后面也要有空格

N = int(input())
list1 = []

for i in range(2,N):
    if N%i == 0:
        list1.append(i)

print(*list1,' ')

# =============================================================================
# # Python program to print list 
# # without using loop 
# 
# a = [1, 2, 3, 4, 5] 
# 
# # printing the list using * operator separated 
# # by space 
# print(*a) 
# 
# # printing the list using * and sep operator 
# print("printing lists separated by commas") 
# 
# print(*a, sep = ", ") 
# 
# # print in new line 
# print("printing lists in new line") 
# 
# print(*a, sep = "\n") 
# =============================================================================
