#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:13:58 2018

@author: xiangyinyu
"""

# 输入一个整数，将这个整数以字符串的形式逆序输出

# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

N = list(input())

Nlist = []
for item in N[::-1]:
    Nlist.append(item)

print(''.join(Nlist))