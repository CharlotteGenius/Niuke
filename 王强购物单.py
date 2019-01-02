#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:06:26 2018

@author: xiangyinyu
"""

# =============================================================================
# 王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，
# 他把想买的物品分为两类：
# 主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
# 主件 	附件
# 电脑 	打印机，扫描仪
# 书柜 	图书
# 书桌 	台灯，文具
# 工作椅 	无 
# 如果要买归类为附件的物品，必须先买该附件所属的主件。
# 每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
# 王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：
# 用整数 1 ~ 5 表示，第 5 等最重要。
# 他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。
# 他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
#     设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，
#     共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，
#     则所求的总和为：
#     v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
#     请你帮助王强设计一个满足要求的购物单。
#
# 输入描述:
# 输入的第 1 行，为两个正整数，用一个空格隔开：N m
# （其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）
# 从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，
# 每行有 3 个非负整数 v p q
# （其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， 
#     q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，
#     如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
#  
# 输出描述:
# 输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（<200000）。
# =============================================================================


# 先来考虑简单的背包问题。
# 假定i是放入的最后一个物品，那么这i个物品构成了当前的最优解
# 如果把i拿走，对（i-1）个物品来说，他们的重量范围是 0~（Weight-iWeight）
# 即：在这个小一点的承重范围内，i-1个物品也是最优解！
# “一个最优解的子集也是最优的！”
# 这样就形成了递归关系！

def Solve(iValue, iWeight, totalItem, totalWeight):
    """
    iValue:        物品的价值，list
    iWeight:       物品的重量，list
    totalItem:     总共放入的物品数量，int
    totalWeight:   背包总承重，int
    i:             第i个物品，总放入物品的子集，int
    w:             背包承重的子集，int
    
    需要求的是最优解 MaxValue[totalItem+,totalWeight+1],
    背包最优解的子集为 MaxValue[i,w] 每个MaxValue[i,w]都达到了最优。
    MaxValue[i,w] will store the maximum (combined) size at most w.
    """
    MaxValue = [ [0 for j in range(totalWeight+1)] for i in range(totalItem+1) ]
# 构建一个行数为背包容量，列数为可用物品的矩阵
# 即最大价值矩阵(横坐标表示[0,totalWeight]整数背包承重):
# (totalItem+1)*(totalWeight+1)
    for i in range(totalItem+1):
    # 历经所有的物品
        for w in range(totalWeight+1):
        # 从小背包到大背包，都满足此时背包的最优解
            if iWeight[i] <= w:
                # 即将放入的项如果比容量小，现在考虑放与不放哪种更优
                MaxValue[i][w] = max(MaxValue[i-1][w-iWeight[i]]+iValue[i], MaxValue[i-1][w])
                """
                MaxValue[i-1][w-iWeight[i]]：
                    这种情况表示如果放了i件物品更优，
                    即没放也是最优，即MaxValue[i-1，W-wi]
                    这时总价值就相当于——没有i时的剩余价值 + i的价值
                MaxValue[i-1][w]：
                    表示在w时，如果不放第i件物品更优，则等于在w中放（i-1）个物品
                    即与MaxValue[i-1,w]价值相等
                """
            else:
                MaxValue[i][w] = MaxValue[i-1][w]
                # 即将放入的项如果比容量大，则不放入，价值不变
    return MaxValue[-1][-1]


# 更优化的理解是
# 现在包的容量为totalWeight，一个一个物品往里装，则i依次增加，而容量w依次减少
def Solve1(iValue, iWeight, totalItem, totalWeight):
    MaxValue = [ 0 for w in range(totalWeight+1) ]
    # 构建一个背包容量的矩阵
    for i in range(0, totalItem+1):
    # 放入的物品增多
        for w in range(totalWeight+1,0,-1):
        # 容量不断减少
            if iWeight[i] <= w:
                MaxValue[w] = max(MaxValue[w], MaxValue[w-iWeight[i]]+iValue[i])
    
    return MaxValue[-1]



# =============================================================================
# 
# =============================================================================

# 回到王强奖金的问题，存在是主件还是附件的条件,这里的每一件物品有三种属性，
# 按照题目的要求写法：价格v，重要度p，主件还是附件q。
'''
价格矩阵:     iCost
重要度矩阵:   iImportance
主附件矩阵:   iQ
钱:          m (from totalMoney to 0)
物品:        i (from 0 to totalItem)
'''
# 首先，此时要求的不是仅仅达到价值的最大值，而是价格iCost与重要度iImportance乘积的最大值！！！
'''
递归条件变为
MaxValue[i][m] = max( MaxValue[i-1][m],  MaxValue[i-1][m-iCost[i]] + iCost[i]*iImportance[i] )
'''

# 其次存在主附件问题。在放第i件时，应首先判断这件物品是主件还是附件，即q是否为0
# 当q为0时，物品为主件，按照上述递归方程直接比较放与不放的价值
# 当q不为0，q的值对应的是主件的编号，此时的重量变为i的重量加上主件q的重量，价值也变为两者价值之和！
'''
递归条件为
MaxValue[i][m] = max( MaxValue[i-1][m],  MaxValue[i-1][ m - 附件价格 - 对应主件价格 ]  +       附件价值            +          对应主件价值            )       
MaxValue[i][m] = max( MaxValue[i-1][m],  MaxValue[i-1][ m -iCost[i]- iCost[iQ[i]] ] + iCost[i]*iImportance[i] + iCost[iQ[i]]*iImportance[iQ[i]])           
'''

def Solve2(iCost, iImportance, iQ, totalItem, totalMoney):
    MaxValue = [0]*(totalMoney+1)
    for i in range(0, totalItem):
    # 购买的物品增多,0表示第一件物品
        for m in range(totalMoney,-1,-10):
        # 钱不断减少,减到0
            if iQ[i] == 0:  #主件
                if iCost[i] <= m:
                    MaxValue[m] = max(MaxValue[m], MaxValue[m-iCost[i]]+iCost[i]*iImportance[i])
            elif iCost[i]+iCost[iQ[i]-1] <= m: #附件
                # iQ[i]-1 因为1表示第一个物品，即数列中0代表的物品，此时的序号需要减1
                MaxValue[m] = max( MaxValue[m],  MaxValue[m-iCost[i]-iCost[iQ[i]-1]] + iCost[i]*iImportance[i] + iCost[iQ[i]-1]*iImportance[iQ[i]-1])
    return MaxValue[-1]

# 输入基本信息，并列成数组
totalMoney, totalItem = map(int,input().strip().split(' '))
# map(function_to_apply, list_of_inputs)
iCost,iImportance,iQ = [],[],[]

for n in range(totalItem):
    v, p, q = map(int,input().strip().split(' '))
    iCost.append(v)
    iImportance.append(p)
    iQ.append(q)

print(Solve2(iCost, iImportance, iQ, totalItem, totalMoney))





