#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:28:49 2018

@author: xiangyinyu
"""

# 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
# 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。 

s1 = input()
s2 = input()
list1 = list(s1)
list2 = list(s2)
# list() is to convert string to list
# string.split() only split ones have the spaces
# eg. "apple egg banana" to ['apple', 'egg', 'banana']

def func(a_list):
    l = len(a_list)
    r = int((l-l%8)/8)
    for n in range(0,r):
        print(''.join(a_list[8*n:8*(n+1)]))
        # ''.join() is to convert list to string
    if l%8 != 0:
        for n in range(0,8-l%8):
            a_list.append('0')
        print(''.join(a_list[8*r:8*(r+1)]))
    
func(list1)
func(list2)