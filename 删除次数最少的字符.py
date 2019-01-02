#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:59:55 2018

@author: xiangyinyu
"""

# =============================================================================
# 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
# 输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。 
# 输入描述:
# 字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
# 
# 输出描述:
# 删除字符串中出现次数最少的字符后的字符串。
# =============================================================================

while True:
    try:
        string = input()
        letter_count = {}
        
        for i in string:
            m = string.count(i)
            letter_count[i] = m
        
        min_count = min(letter_count.values())
        for letter in string:
            if letter_count[letter] == min_count:
                string = string.replace(letter,'')
        
        print(string)
    except:
        break