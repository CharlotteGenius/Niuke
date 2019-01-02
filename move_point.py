#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:16:01 2018

@author: xiangyinyu
"""

# =============================================================================
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，
# W表示向上移动，S表示向下移动。从（0,0）点开始移动，
# 从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
# 输入：
# 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
# 坐标之间以;分隔。
# 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
# 输入描述:
# 一行字符串
# 输出描述:
# 最终坐标，以,分隔
# =============================================================================

def movement(moves):
    x, y = 0, 0
    for move in moves:
        if len(move) > 1:
            if move[0]=='A' or 'S' or 'D' or 'W':
                l = len(move)
                if move[1:l+1].isdigit():
                    if move[0]=='A':
                        x = x-int(move[1:l+1])
                    if move[0]=='S':
                        y = y-int(move[1:l+1])
                    if move[0]=='D':
                        x = x+int(move[1:l+1])
                    if move[0]=='W':
                        y = y+int(move[1:l+1])
    return x,y

moves = input().strip().split(';')
print("%d,%d"%(movement(moves)[0],movement(moves)[1]))