#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:19:45 2018

@author: xiangyinyu
"""

#明明想在学校中请一些同学一起做一项问卷调查，
#为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000）
#对于其中重复的数字，只保留一个，把其余相同的数去掉，
#不同的数对应着不同的学生的学号。
#然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。
#请你协助明明完成“去重”与“排序”的工作
#(同一个测试用例里可能会有多组数据，希望大家能正确处理)。

# 以下为输入输出示例：
# =============================================================================
# Input Param：
# n               输入随机数的个数
# inputArray      n个随机整数组成的数组
# 
# Return Value：
# OutputArray    输出处理后的随机整数
# =============================================================================

import random as rd

# 运用递归的方法建立加入学生的函数
def add_student(a_list):
    a_student = int(input())
    if a_student <= 1000 and a_student >= 1:
        a_list.append(a_student)
    else:
        add_student(a_list)

# list1中包含了N个输入的学生
N = int(input())
list1 = []
for n in range(N):
    add_student(list1)
print(list1)
    
# 将相同项设置为‘repeat’再进行统一删除
for a in range(N):
    for b in range(a+1,N):
        if list1[a] == list1[b]:
            list1[b] = 'repeat'
print(list1)
# 删除所有的‘repeat’
# python中的remove（）只删除第一个出现的值而不删除全部
#list1[:] = (value for value in list1 if value != 'repeat')

while 'repeat' in list1:
    list1.remove('repeat')
# 这两种方法都可以去掉list中的所有此项
print(list1)


# 新的数列长度
l = len(list1)

# =============================================================================
# 排序
# =============================================================================

# 1. Bubble Sort 冒泡法
# 重复地走访过要排序的数列，一次比较两个元素，
# 如果它们的顺序错误就把它们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 每走完一次就将沉淀一个最大数在末尾，那么下一次只需要走前面剩下的较小数。
# 则 走访整个数列的次数为l-1次
def bubbleSort(a_list):
    for a in range(l-1):
        for i in range(0,l-1-a):
            # l-1-a 表示已有a个数已经沉淀，只需在前面的数中比较
            if a_list[i] > a_list[i+1]:
                temp = a_list[i+1]
                a_list[i+1] = a_list[i]
                a_list[i] = temp
                # 两两比较并交换较小值到前面
    return a_list

# =============================================================================
# 
# =============================================================================
# 2. Selection Sort 选择排序
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
def selectionSort(a_list):
    for a in range(l):
        minIndex = a
        for b in range(a+1,l):
            if a_list[b] < a_list[minIndex]:
                minIndex = b
                # 找到最小数的索引
        temp = a_list[minIndex]
        a_list[minIndex] = a_list[a]
        a_list[a] = temp
        # 将最小数与前排进行调换
    return a_list

# =============================================================================
# 
# =============================================================================
# 3. Insertion Sort 插入排序
# 构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
def insertionSort(a_list):
    for a in range(1,l):
        preIndex = a - 1
        current = a_list[a]
        # 设置current是将a数抽出，而此时a的位置是可以放入其他数的
        # 即，a位空出，而a数则是current，便于将大于a数的已排序数移到a位
        while preIndex >= 0 and a_list[preIndex] > current:
        # preIndex为已排序数列的数的索引
        # a 是已排序数列的后一位 的索引
            a_list[preIndex+1] = a_list[preIndex]
        # 已排序数从右往左依次与目标数a进行比较，当该数大于a数时，
        # 将该数往右移动一位
            preIndex = preIndex - 1
        # 将索引往前移动，继续比较
        # 一直比较到已排序的那个数不大于a数时，跳出循环
        a_list[preIndex+1] = current
        # 将a数放在该不大于a数的已排序数的后面一位
        # 此时完成了一步的排序，此时a变成a+1，即选择下一个a数再次排序
    return a_list

# =============================================================================
#   
# =============================================================================
# 4. Shell Sort 希尔排序
# 是简单插入排序的改进版。它与插入排序的不同之处在于：
# 它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
# 确定一个增量t，将数列中[0,t,2t,...], [1,t+1,2t+1,...], ...分组取出
# 依次在这些小分组中进行插入排序
# 即简单的插入方法为：一位一位的向前比较，找到比自己小的一项时，插入在此项后方一位
# 此方法为：t位t位的向前比较，找到比自己小的一项时，插入在此项后方t位
# 每进行一轮分组排序，减小t，再重复 分组 插入排序
# 到最后一轮时，t 已经减小为 1，即:将整个数列作为一个序列来处理，这一轮与简单插入没有区别
# 但由于已经进行了前面的分组处理，这一步的比较会减少很多
def shellSort(a_list):
    t = rd.randint(1,l)
    # 随便选的一个初始增量，好像选谁都行。。。不知道选谁效率达到最高
    while t>0:
        for a in range(t,l):
            preIndex = a - t
            current = a_list[a] #待比较的a数
            while preIndex >= 0 and a_list[preIndex] > current:
                a_list[preIndex+t] = a_list[preIndex]
                preIndex = preIndex - t
            a_list[preIndex+t] = current
        t = t//2
    return a_list

# =============================================================================
# 
# =============================================================================
# 5. Merge Sort 归并排序

# 将已有序的子序列合并，得到完全有序的序列；
# 即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 
# Merge sort is a recursive algorithm that continually splits a list in half. 
# If the list is empty or has one item, it is sorted by definition (the base case). 
# If the list has more than one item, 
# we split the list and recursively invoke a merge sort on both halves. 
# Once the two halves are sorted, the fundamental operation, 
# called a merge, is performed.  
# Merging is the process of taking two smaller sorted lists and 
# combining them together into a single, sorted, new list.

def mergeSort(a_list):
    # splitting.....
    if len(a_list) > 1:
        mid = len(a_list)//2
        left_half = a_list[0:mid]
        right_half = a_list[mid:len(a_list)]
        # split the list into two halves

        mergeSort(left_half)
        mergeSort(right_half)
        # Here, call the function for two halves, 
        # So suppose the two halves are already sorted, 
        # now we just do the merging!
        
        a = 0
        b = 0
        k = 0
        while a < len(left_half) and b < len(right_half):
            if left_half[a] < right_half[b]:
                a_list[k] = left_half[a]
                a = a+1
            else:
                a_list[k] = right_half[b]
                b = b+1
            k = k+1
    
        while a < len(left_half): # and b == len(right_half):
            # that's to say, b = l_ri here, right half are completely sorted
            # but some values are unsorted in left half
            # so we simply add the left values add the end of the list
            a_list[k] = left_half[a]
            a = a+1
            k = k+1
            
        while b < len(right_half): # and a == len(left_half):
            a_list[k] = right_half[b]
            b = b+1
            k = k+1
    # Merging.....

# 归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，
# 但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。


# =============================================================================
# 
# =============================================================================
# 6. Quick Sort 快速排序
# 快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，
# 所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
# 在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    # 1. bring the pivot to its apropriate position such that
    #    left of it is smaller and right is larger
    # 2. quick sort the left part
    # 3. quick sort the right part
    
def quickSort(a_list):
    if len(a_list) > 0:
        
        p = 0
        while p < l:
            pivot = a_list[p]
            for a in range(p+1,l):
                i = 0
                if a_list[a] < pivot:
                    temp = a_list[a]
                    a_list[p+1:a+1] = a_list[p:a]
                    a_list[p] = temp
                    i = i+1
            # 较小的a数移到基准左边一位    
            p = p+i
        return a_list

list2 = [22,33,34,2,4,2,5,7,8,4,6,10]
l = len(list2)
quickSort(list2)
print(list2)