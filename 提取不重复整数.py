#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:27:13 2018

@author: xiangyinyu
"""
# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

N = list(input())
pout = []
for item in N[::-1]:
# 对于一个list，list[a:b:c]表示的是：
# a是开始的值，b是结尾的值，c是跳的位数
# 例如：list[1:10:2]
# 则是有第 1,3,5,7,9 这些项
# 此题的 -1 代表的是倒叙跳跃一步！！！
    if item not in pout:
        pout.append(item)

print(int(''.join(pout)))