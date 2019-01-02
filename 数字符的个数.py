#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 00:55:09 2018

@author: xiangyinyu
"""

# 写出一个程序，接受一个由字母和数字组成的字符串，
# 和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。


string = input()
char = input()

print(string.lower().count(char.lower()))


