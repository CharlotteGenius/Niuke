#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:03:35 2019

@author: xiangyinyu
"""
# 答题规范 ##

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)

import sys
if __name__ == "__main__":
    num = sys.stdin.readline().strip()
    a = int(num.split()[0])
    b = int(num.split()[1])
    print(a+b)
    


# 应该这样来实现多行输入
while True:
    num = sys.stdin.readline().strip()
    if not num:
        break
    
# 或者...    
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
    

# 又或者...
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(int(lines[0]) + int(lines[1]))
except:
    pass