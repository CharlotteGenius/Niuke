#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 00:35:22 2018

@author: xiangyinyu
"""

string = input()
if string != None and len(string) < 5000:
    N = len(string.split()[-1])
print(N)