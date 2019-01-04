#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:00:21 2019

@author: xiangyinyu
"""

# =============================================================================
# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# 
#     /**
#      * 统计出兔子总数。
#      * 
#      * @param monthCount 第几个月
#      * @return 兔子总数
#      */
#     public static int getTotalCount(int monthCount)
#     {
#         return 0;
#     }
# 
# 输入描述:
# 输入int型表示month
# 
# 输出描述:
# 输出兔子总数int型
# =============================================================================

    
# =============================================================================
# def bunny(n):
#     if n<=2:
#         return 1
#     elif n>2:
#         return bunny(n-1) + bunny(n-2)
# while True:
#     try:
#         k=int(input())
#         print(bunny(k))
#     except:
#         break
# =============================================================================

def bunny(n):
    age = [1]
    print(age)
    for i in range(1,n):
        # 经历的月份
        for j in range(len(age)):
            age[j] = age[j]+1
            # 每只兔子年龄+1
            if age[j] >=3:
                age.append(1)
                # 如果兔子j成熟了，那么j生一只，兔子群里加一只年龄为1的兔子
        print(age)           
    return len(age)
        
while True:
    try:
        k=int(input())
        print(bunny(k))
    except:
        break
