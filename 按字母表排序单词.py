#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:42:16 2018

@author: xiangyinyu
"""

# 给定n个字符串，请对n个字符串按照字典序排列。
# 输入描述:
# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
# 输出描述:
# 数据输出n行，输出结果为按照字典序排列的字符串。

num = int(input())
word = []
for n in range(num):
    word.append(input())

word_sort = [value for value in word]
#word_sort = sorted(word_sort) 两种写法都可以
word_sort.sort()

for item in word_sort:
    print(item)

