#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 22:30:10 2018

@author: xiangyinyu
"""

# =============================================================================
# 计算最少出列多少位同学，使得剩下的同学排成合唱队形
# 
# 说明：
# N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。 
# 合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，
# 他们的身高分别为T1，T2，…，TK，
# 则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。 
# 你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。 
# 
# 输入描述:
# 整数N
# 
# 输出描述:
# 最少需要几位同学出列
# =============================================================================

import bisect
# This module provides support for maintaining a list in sorted order 
# without having to sort the list after each insertion.

def deal(heights,result):
    # 每次向deal中加一个身高元素
    deal = [9999]*len(heights)
    # 初始设为一些比正常身高都大的数
    deal[0] = heights[0]
    result = result + [1]
    
    JIARUYIHANG
    
# =============================================================================
#     for i in range(1,len(heights)):
# =============================================================================
        pos = bisect.bisect_left(deal,heights[i]) 
        
        # bisect.bisect_left(a, x, lo=0, hi=len(a))
        # If x is already present in a, the insertion point will be before 
        # (to the left of) any existing entries.
        # the returned insertion point i:
        # all(val < x for val in a[lo:i]) for the left side and 
        # all(val >= x for val in a[i:hi]) for the right side.
        # 这样的过程使整个数列按从小到大排列,pos为得到的i点
        
        # bisect.bisect_right(a, x, lo=0, hi=len(a))
        # all(val <= x for val in a[lo:i]) for the left side 
        # and all(val > x for val in a[i:hi]) for the right side.

        result = result + [pos+1]
        # pos本来指的是该数的位置，但result记录的是这个数构成的递增数列的slice
        # 比如原本deal为 [150，160，500] 需要插入下一个数为170
        # 那么170插入的pos为2，那么对于170来说，构成递增数列为[150, 160, 170]
        # 那么对于170的slice为3，即170的位置+1！
        # 此时在result里面加上3这个元素，代表了170的递增数列slice长度！
        
        # 反向处理时，找到的是对于170的递减slice的长度。
        # 比如反向时 找到的170的slice为[130, 140, 170],170的位置是2
        # 代表递减数列为[170, 140, 130]
        # 长度为3，是该数的位置+1
        # 那么我们最终要找的数列就为[150, 160, 170, 140, 130]，长度为5
        # 是 3+3-1 ，需要减去170重复计算的那一次。
        
        deal[pos] = heights[i]
        # 解释一通后发现说不清楚...自己多举几个例子看看吧...

    return result
    
while True:
    try:
        n = int(input())
        heights = list(map(int,input().split()))
        dp1=[]
        dp2=[]
        dp1 =deal(heights,dp1)#正序遍历位置
        dp2=deal(heights[::-1],dp2)[::-1]#逆序遍历位置
        
        a = max(dp1[i]+dp2[i]for i in range(n))#两次遍历的结果相加
        print(n-a+1)#a中的那个人多加了一次 故要+1
    except:
        break


# =============================================================================
# 首先计算每个数在最大递增子串中的位置：
# 
# 186  186  150  200  160  130  197  200   quene
# 1    1    1     2    2    1    3   4     递增计数
# 
# 
# 然后计算每个数在反向最大递减子串中的位置--->计算反向后每个数在最大递增子串中的位置：
# 
# 200  197  130  160  200  150  186  186   反向quene
# 1     1    1    2    3    2    3    3     递减计数
# 
# 
# 然后将每个数的递增计数和递减计数相加：
#
# 186  186  150  200  160  130  197  200   quene
# 1      1      1      2       2     1      3      4       递增计数
# 3      3      2      3       2     1      1      1       递减计数
# 4      4      3      5       4     2      4      5       每个数在所在队列的人数+1（自己在递增和递减中被重复计算）
# 
# 
# 如160这个数，在递增队列中有2个人数
# 150  160
# 在递减队列中有2个人数
# 160  130
# 那么160所在队列中就有3个人
# 150  160  130
# 每个数的所在队列人数表达就是这个意思
# 总人数 - 该数所在队列人数 = 需要出队的人数
# =============================================================================


