#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:21:04 2018

@author: xiangyinyu
"""
'''
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址1.0.0.0~126.255.255.255;
B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255;
D类地址224.0.0.0~239.255.255.255；
E类地址240.0.0.0~255.255.255.255
私网IP范围是：
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255

子网掩码为前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
本题暂时默认以0开头的IP地址是合法的，比如0.1.1.2，是合法地址

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''
import sys

def check_ip(ip):
    if len(ip) != 4:
        return False
    else:
        for i in range(4):
            if i<0 or i>255:
                return False
        else:
            return True

def check_mask(mask):
    # reference (subnet mask):
    # https://doc.m0n0.ch/quickstartpc/intro-CIDR.html
    # 这一题我把255放入list网页显示答案不同，然后我就去掉了255
    # 说明题目默认255.255.255.255不是合法的掩码
    check_list = [254, 252, 248, 240, 224, 192, 128, 0]
    if mask[0] == 255:
        if mask[1] == 255:
            if mask[2] == 255:
                if mask[3] in check_list:
                    return True
                else:
                    return False
            elif mask[2] in check_list and mask[3] == 0:
                return True
            else:
                return False
        elif mask[1] in check_list and mask[2] == 0 and mask[3] == 0:
            return True
        else:
            return False
    elif mask[0] in check_list and mask[1] == 0 and mask[2] == 0 and mask[3] == 0:
        return True
    else:
        return False

A = 0
B = 0
C = 0
D = 0
E = 0
err = 0
private_ip = 0

while True:
    string = sys.stdin.readlines().strip()
    if not string:
       break
    # 由于题目要求的是一次输入多行，我们在这里要用
    # sys.stdin.readline().strip()
    # strip()是为了去掉多余的函数和空格占的空间
    # 因为sys.stdin.readline()会将输入的\n也算入其中
    # 在spyder里面不知道为什么不管用...但是页面里运行是ok的...
    a = string.split('~')[0]
    b = string.split('~')[1]
    ip = [int(i) for i in a.split('.')]
    mask = [int(i) for i in b.split('.')]
    
    if check_ip(ip) and check_mask(mask):
        if ip[0]>=1 and ip[0]<=126:# A类
            A = A+1
            if ip[0] == 10:
                private_ip = private_ip+1
        if ip[0]>=128 and ip[0]<=191:# B类
            B = B+1
            if ip[0] == 172 and ip[1]>=16 and ip[1]<=31:
                private_ip = private_ip+1
        if ip[0]>=192 and ip[0]<=223:# C类
            C = C+1
            if ip[0] == 192 and ip[1] == 168:
                private_ip = private_ip+1
        if ip[0]>=224 and ip[0]<=239:# D类
            D = D+1
        if ip[0]>=240 and ip[0]<=255:# E类
            E = E+1
    else:
        err = err+1
    print(A, B, C, D, E, err, private_ip)
