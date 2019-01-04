#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:10:12 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目描述
# 对字符串中的所有单词进行倒排。
# 
# 说明：
# 1、每个单词是以26个大写或小写英文字母构成；
# 2、非构成单词的字符均视为单词间隔符；
# 3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，
#     倒排转换后也只允许出现一个空格间隔符；
# 4、每个单词最长20个字母；
# 
# 输入描述:
# 输入一行以空格来分隔的句子
# 
# 输出描述:
# 输出句子的逆序
# =============================================================================

while True:
    try:
        string = list(input().strip())
        for i in range(len(string)):
            if not string[i].isalpha():
                string[i] = ' '
        string = ''.join(string)
        rev_string = string.split()[::-1]
        print(' '.join(rev_string))
    except:
        break

