#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:17:44 2018

@author: xiangyinyu
"""

# 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
# 即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

# 输入描述:
# 先输入键值对的个数
# 然后输入成对的index和value值，以空格隔开

# 输出描述:
# 输出合并后的键值对（多行

num = int(input())
sheet = {}

for n in range(num):
    key, value = input().split(' ')
    key = int(key)
    value = int(value)
    sheet[key] = sheet.setdefault(key, 0) + value
    # add a default key with the name: "key" and the value: 0
    # add 0 with the value input
    # notice!: set the default value as 0 and then do the sum
    # dict.setdefault(key, default_value)
    # if defaulf_value is not set, it's set to be none, not 0!
    # 第一次设置该key为0以后，下次再调用setdefault()时，并不会再次把该key的值设置为0
    # 例如：
# =============================================================================
#     a = {'age':2}
#     a['age'] = a.setdefault('age',0)
#     print(a)
#     结果依然是 a = {'age':2}
# =============================================================================
    # 当dict里面已经含有某个key时，调用此函数，对dict没有影响！！！！！！
    
for a_key in sorted(sheet.keys()):
    print(a_key, sheet[a_key])
    
    
    