#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:06:30 2018

@author: xiangyinyu
"""

# 编写一个函数，计算字符串中含有的不同字符的个数。
# 字符在ACSII码范围内(0~127)。不在范围内的不作统计。

# =============================================================================
# # Get the ASCII number of a character:
# number = ord(char)
# 
# # Get the character given by an ASCII number:
# char = chr(number)
# =============================================================================

acsii = list(input())

Number = []
count = 0
for char in acsii:
    if ord(char) not in Number:
        Number.append(ord(char))
        count = count+1
print(count)