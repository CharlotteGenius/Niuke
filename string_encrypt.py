#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:10:13 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目描述
# 对输入的字符串进行加解密，并输出。
# 加密方法为：
# 当内容是英文字母时则用该英文字母的后一个字母替换，
# 同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
# 当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
# 其他字符不做变化。
# 
# 解密方法为加密的逆过程。
# 接口描述：
#     实现接口，每个接口实现1个基本操作：
# 
# void Encrypt (char aucPassword[], char aucResult[])：
# 在该函数中实现字符串加密并输出
# 1、字符串以\0结尾。
# 2、字符串最长100个字符。
# 
# int unEncrypt (char result[], char password[])：
# 在该函数中实现字符串解密并输出
# 1、字符串以\0结尾。
# 2、字符串最长100个字符。
# =============================================================================

# I tested in console and get...
'''
ord('A')
Out[1]: 65

ord('a')
Out[2]: 97

ord('B')
Out[3]: 66

ord('b')
Out[4]: 98

ord('Z')
Out[5]: 90

ord('z')
Out[6]: 122
'''
# so we can use acsii code here!

def Encrypt(Password):
    Result = Password
    for i in range(len(Password)):
        if Password[i].isupper():
            if Password[i] == 'Z':
                Result[i] = 'a'
            else:
                Result[i] = chr(ord(Password[i])+33)
            
        elif Password[i].islower():
            if Password[i] == 'z':
                Result[i] = 'A'
            else:
                Result[i] = chr(ord(Password[i])-31)
            
        elif Password[i].isdigit():
            if Password[i] == '9':
                Result[i] = '0'
            else:
                Result[i] = str(int(Password[i])+1)    
    return Result


def unEncrypt(Result):
    Password = Result
    for i in range(len(Result)):
        if Result[i].isupper():
            if Result[i] == 'A':
                Password[i] = 'z'
            else:
                Password[i] = chr(ord(Result[i])+31)
            
        elif Result[i].islower():
            if Result[i] == 'a':
                Password[i] = 'Z'
            else:
                Password[i] = chr(ord(Result[i])-33)
            
        elif Result[i].isdigit():
            if Result[i] == '0':
                Password[i] = '9'
            else:
                Password[i] = str(int(Result[i])-1)
    return Password

while True:
    try:
        psw = list(input())
        rslt = list(input())
        print(''.join(Encrypt(psw)))
        print(''.join(unEncrypt(rslt)))
    except:
        break
