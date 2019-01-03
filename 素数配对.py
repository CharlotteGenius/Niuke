#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:49:08 2019

@author: xiangyinyu
"""

# =============================================================================
# 题目描述
# 若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，
# 如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，
# 从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，
# 挑选方案多种多样，例如有4个正整数：2，5，6，13，
# 如果将5和6分为一组中只能得到一组“素数伴侣”，
# 而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”
# 最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
# 
# 输入:
# 有一个正偶数N（N≤100），表示待挑选的自然数的个数.
# 后面给出具体的数字，范围为[2,30000]。
# 
# 输出:
# 输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。
# 
# 输入描述:
# 输入说明
# 1 输入一个正偶数n
# 2 输入n个整数
# 
# 输出描述:
# 求得的“最佳方案”组成“素数伴侣”的对数。
# =============================================================================


def prime_num(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
# prime number check---------------------------------------------

def parity(numbers):
    odd = []
    even = []
    for num in numbers:
        if num%2 == 0:
            even.append(num)
        if num%2 != 0:
            odd.append(num)
    return odd,even
# seperate numbers into odd and even numbers---------------------
    
def matrix(odd,even):
    matrix_2d = [[0 for i in range(len(odd))] for i in range(len(even))]
    for i in range(len(odd)):
        for j in range(len(even)):
            if prime_num(odd[i]+even[j]):
                matrix_2d[j][i] = 1
                # 注意先找行再找列，偶为行，奇为列
    
    # build a 2d matrix, set the numbers 0
    # if make a prime number pair, set it to 1
    return matrix_2d
# 2d matrix-------------------------------------------------------

def find(e):
    # 我现在是偶数，要去找奇数
    for o in range(len(odd)):
        if matrix[e][o] and (not visited[o]):
            # 若奇偶可连，且奇数没被访问过
            visited[o] = 1
            # 表示我现在即刻访问该奇数
            if connect[o] == -1 or find(connect[o])!= 0:
            # 访问：是否被连？或：你连的那个数能不能连别的？
            # 如果该奇数被连接了，但其连接的那个偶数 能找到另一个连接的奇数，那么执行以下
                connect[o] = e
                return True
                # 表示匹配
    return False
# 当我是某一个偶数时，我找奇数的整个过程，使用同一个used
# 当我变成下一个偶数时，visitsed要全部置零，但connect不同
# visited保证了 在交替寻找直到找到可以连接的交替点时，不会重复访问/走重复的交替路线
        # 但对于下一个偶数而言，即使访问上一个偶数被访问的奇数，也不是同样的路径，所以每一次都需要置零
# connect则表示了 该奇数是否被连接，所以是整个匹配过程的函数
        # 如果连接，不代表不能连接，而要交替路径直到找到可连接数
# 这是匈牙利算法，重点在于“交替”的过程

while True:
    try:
        N = input()
        numbers = list(map(int, input().split()))
        odd,even = parity(numbers)
        matrix = matrix(odd,even)
        # 构建好两个数组
        
        count = 0
        connect = [-1 for i in range(len(odd))]
        for e in range(len(even)):
            visited = [0 for i in range(len(odd))]
            # 以上都是find()的全局变量
            if find(e):
                count = count+1
            # 如果某个连接并非最佳连接，那它一定会被后面的连接挤掉
            # 如果没有被挤掉，说明数量上也达到最优，此时不必纠结于配对的是谁
            # 只需要着眼于count计数
            # 因为即使挤掉了，对count并无影响
        print(count)
    except:
        break
    
    