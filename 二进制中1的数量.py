#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:00:55 2018

@author: xiangyinyu
"""


# 输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

N = int(input())
N_bin = bin(N)
N_list = list(N_bin)

print(N_list.count('1'))