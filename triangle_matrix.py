#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:12:52 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目说明：
# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
# 
# 样例输入：
# 5
# 
# 样例输出：
# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11
# 
# 样例输入:
# 4
# 
# 样例输出:
# 1 3 6 10
# 2 5 9
# 4 8
# 7
# 
# 输入参数：
#         int Num：输入的正整数N(不大于100)
# 输出参数：
#         输出一个N行的蛇形矩阵。
# =============================================================================

def triangle_matrix(Num):
    matrix = [[] for n in range(Num)]
    matrix[0].append(1)
    for i in range(1,Num):
        matrix[0].append(matrix[0][i-1]+i+1)
    # 先建好第一行
    
    for n in range(1,Num):
        # 从第2行开始,n=1
        matrix[n].append(matrix[n-1][0]+n)
        # 每一行的第一个数
        for i in range(1,Num-n):
            # n=1行时，有Num-1个数
            # n=2行时，有Num-2个数....
            matrix[n].append(matrix[n][i-1]+n+i+1)
    
    return matrix

while True:
    try:
        N = int(input())
        tri_m = triangle_matrix(N)
        for m in tri_m:
            m = [str(x) for x in m]
            print(' '.join(m))
    except:
        break
    
