#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:19:08 2018

@author: xiangyinyu
"""

# 知某次聚会敏感词有N个人参加，这N个人来自26个地区，
# 现在将26个地区使用数字0-25表示，使用整数数组Locations存储这N个人的地区, 
# 请返回一个bool值, True代表所有人的地区全都不同，False代表存在相同地区。
# 要求：不能使用额外的存储结构。


import random as rd

N = int(input("How many people went to the party?:"))
Locations = []

for n in range(N):
    n = rd.randint(0,26)
    Locations.append(n)
print(Locations)

# =============================================================================
# Bool1 = True
# Bool2 = True
# 
# # Solution 1:
# for a in range(N):
#     for b in range(N):
#         if a!=b and Locations[a]==Locations[b]:
#             Bool1 = False
# 
# # Solution 2:
# for a in range(N):
#     for b in range(a+1,N):
#         if Locations[a]==Locations[b]:
#             Bool2 = False
#             break
# 
# print(Bool1,Bool2)
# =============================================================================


# 由于题目要求不能用另外的存储空间
# 以上两种方法用了Bool1和Bool2，所以不符合题目要求
# 于是我又开始写下面的代码.......


def no_same_location():
    for a in range(N):
        for b in range(a+1,N):
            if Locations[a]==Locations[b]:
                return False
    return True
            
print(no_same_location())