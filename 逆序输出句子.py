#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:32:35 2018

@author: xiangyinyu
"""

# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
sentence = input()
def sentence_reverse(sentence):
    sentence_list = sentence.split()
    sentence_reverse_list = []
    for item in sentence_list[::-1]:
        sentence_reverse_list.append(item)
    return ' '.join(sentence_reverse_list)

print(sentence_reverse(sentence))