#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:48:15 2018

@author: xiangyinyu
"""

# =============================================================================
# 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
# 假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，
# 他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，
# 怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
# 他是这么变换的，大家都知道手机上的字母： 
# 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, 
# pqrs--7, tuv--8 wxyz--9, 0--0,
# 就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
# 声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，
# 如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
# =============================================================================

psw = list(input())

for i in range(len(psw)):
    if psw[i] in 'abc':
        psw[i] = '2'
    if psw[i] in 'def':
        psw[i] = '3'
    if psw[i] in 'ghi':
        psw[i] = '4'
    if psw[i] in 'jkl':
        psw[i] = '5'
    if psw[i] in 'mno':
        psw[i] = '6'
    if psw[i] in 'pqrs':
        psw[i] = '7'
    if psw[i] in 'tuv':
        psw[i] = '8'
    if psw[i] in 'wxyz':
        psw[i] = '9'
    if psw[i].isupper():
        if psw[i] == 'Z':
            psw[i] = 'a'
        else:
            psw[i] = chr(ord(psw[i]) + 1).lower()

print(''.join(psw))
