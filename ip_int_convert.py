#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:21:11 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目描述
# 原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，
#     然后把这个二进制数转变成一个长整数。
# 
# 举例：一个ip地址为 10.0.3.193
# 每段数字             相对应的二进制数
# 10                   00001010
# 0                    00000000
# 3                    00000011
# 193                  11000001
# 
# 组合起来即为：00001010 00000000 00000011 11000001,
# 转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
# 
# 输入描述:
# 输入 
# 1 输入IP地址
# 2 输入10进制型的IP地址
# 
# 输出描述:
# 输出
# 1 输出转换成10进制的IP地址
# 2 输出转换后的IP地址
# =============================================================================


def TransDec(IP):
    number = list(map(int,IP.split('.')))
    Binary = ''
    for n in range(4):
        binary = bin(number[n])[2:]
        if len(binary) < 8:
            binary = '0'*(8-len(binary))+binary   
            # 8 digits binary
        Binary = Binary + binary
    Decimal = int(Binary,2)
    return Decimal




def TransIP(Dec):
    Binary = bin(Dec)[2:]
    number = []
    if len(Binary) < 32:
        Binary = '0'*(32-len(Binary))+Binary
    for a in range(0,len(Binary),8):
        slc = Binary[a:a+8]
        number.append(str(int(slc,2)))

    IP = '.'.join(number)
    return IP

while True:
    try:
        ip = input().strip()
        dec = int(input().strip())
        
        print(TransDec(ip))
        print(TransIP(dec))
    except:
        break
