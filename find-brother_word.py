#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:51:15 2019

@author: yeldon
"""

while True:
    try:
        string = input().strip().split()
        
        dictionary = string[1:-2]
        n = int(string[-1])
        word = string[-2]
        
        bros = []
        for w in range(len(dictionary)):
            if sorted(dictionary[w]) == sorted(word) and dictionary[w] != word:
                bros.append(dictionary[w])
        bros = sorted(bros)
        
        if n<=len(bros):
            print(len(bros))
            print(bros[n-1])
    except:
        break