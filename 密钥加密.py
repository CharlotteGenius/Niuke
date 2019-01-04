#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:11:11 2019

@author: xiangyinyu
"""

# =============================================================================
# 有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。
# 
# 下面是它的工作原理：
# 首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，
# 只保留第1个，其余几个丢弃。现在，修改过的那个单词属于字母表的下面，如下所示：
# 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# 
# T R A I L B Z E S C D F G H J K M N O P Q U V W X Y
# 
# 上面其他用字母表中剩余的字母填充完整。
# 在对信息进行加密时，信息中的每个字母被固定于顶上那行，
# 并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。
# 因此，使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。
# 
# 
# 输入描述:
# 先输入key和要加密的字符串
# 
# 输出描述:
# 返回加密后的字符串
# =============================================================================


def Encrypt(Key,string):
    org_alpha = [chr(x) for x in range(65,91)]
    # original alphabet--------------------------------------
    
    new_alpha = Key
    for a in org_alpha:
        if a not in Key:
            new_alpha.append(a)
    # create a new alphabet which is the KEY-----------------
    
    for i in range(len(string)):
        if string[i].isupper():
            pos = org_alpha.index(string[i])
            string[i] = new_alpha[pos]
        elif string[i].islower():
            pos = org_alpha.index(string[i].upper())
            string[i] = new_alpha[pos].lower()
            
    return ''.join(string)

while True:
    try:
        input_key = [ x.upper() for x in list(input()) ]
        key = []
        for k in input_key:
            if k not in key:
                key.append(k.upper())
        
        psw = list(input())
        print(Encrypt(key,psw))
    except:
        break
    