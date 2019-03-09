#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:13:25 2019

@author: xiangyinyu
"""

# =============================================================================
# 按照指定规则对输入的字符串进行处理。
# 
# 将输入的两个字符串 - 合并、排序、转换！
# 
# 排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。
# 这里的下标意思是字符在字符串中的位置。
# 
# 转换，要求为：如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，
# 则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。
# 如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 
# 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
# 
# 举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，
# 分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
# 
# 接口设计及说明：
# 
# 输入:
# 两个字符串,需要异常处理
# 
# void ProcessString(char* str1,char *str2,char * strOutput)
# 
# 输出:
# 输出转化后的结果
# =============================================================================


def Join(string1,string2):
    strings = string1 + string2
    return strings
# return a string


def Sort(string):
    L = len(string)
    string1 = []
    string2 = []
    string_sort = list(string)
    
    for i in range(0,L,2):
    # 0,2,4,6,...
        string1.append(string[i])
    string1 = sorted(string1)
    print(string1)
    for a in range(0,L,2):
        string_sort[a] = string1[a//2]
        # string_sort[0,2,4,6,...] = string1[0,1,2,3,...]
    # odd position
    
    for j in range(1,L,2):
    # 1,3,5,...
        string2.append(string[j])
    string2 = sorted(string2)
    print(string2)
    for b in range(1,L,2):
        string_sort[b] = string2[(b+1)//2-1]
        # string_sort[1,3,5,...] = string1[0,1,2,3,...]
    # even position
    print(string_sort)
    return string_sort
# return a list!
    

def Trans(string):
    string_trans = string
    for i in range(len(string)):
        if string[i].isdigit() or (string[i] in 'ABCDEFabcdef'):
            binary = bin(int(string[i],16))[2:]
            if len(binary)!=4:
            # remember to add 0 to make 4 digits!
                binary = '0'*(4-len(binary))+binary
            print(binary)
            string_trans[i] = hex(int(binary[::-1],2))[-1]
            print(string_trans[i])
        # reverse, and remember to remove '0x' at the begnning
            if string_trans[i].islower():
                string_trans[i] = string_trans[i].upper()
    return ''.join(string_trans)
# input what, return what
    

str1, str2 = input().strip().split()
str_join = Join(str1,str2)
str_sort = Sort(str_join)
str_trans = Trans(str_sort)

print(str_trans)



