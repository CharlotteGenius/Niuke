#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 09:35:22 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目描述
# 编写一个程序，将输入字符串中的字符按如下规则排序。
# 
# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
#        如，输入： Type   输出： epTy
# 
# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
#      如，输入： BabA   输出： aABb
# 
# 规则 3 ：非英文字母的其它字符保持原来的位置。
#      如，输入： By?e   输出： Be?y
# 
# 样例：
#     输入：
#    A Famous Saying: Much Ado About Nothing(2012/8).
#     输出：
#    A  aaAAbc   dFgghh :  iimM   nNn   oooos   Sttuuuy  (2012/8).
# =============================================================================

while True:
    try:
        string = list(input())
        lower = []
        
        for i in range(len(string)):
            if string[i].isalpha():
               lower.append((string[i].lower(),i))
        
        lower = sorted(lower)
        
        for i in range(len(string)):
            for j in range(len(lower)):
                if string[i].isupper() and i == lower[j][1]:
                    lower[j] = (string[i],i)
        
        Alpha = [x[0] for x in lower]
        i = 0
        for a in range(len(string)):
            if string[a].isalpha():
                string[a] = Alpha[i]
                i = i+1
                
        print(''.join(string))   
    except:
        break

