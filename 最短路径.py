#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:06:03 2019

@author: xiangyinyu
"""

import sys

def Find(row,col,ax,ay,bx,by,blks):
    distance = [[9999 for c in col] for r in row]
    distance[ax][ay] = 0
    x = ax
    y = ay
    for blk in blks:
        if (x,y) != blk:
            distance[x+1][y] = distance[x][y]+1
            x = x+1
    for blk in blks:
        if (x,y) != blk:
            distance[x][y+1] = distance[x][y]+1
    for blk in blks:
        if (x,y) != blk:
            distance[x-1][y] = distance[x][y]+1
    for blk in blks:
        if (x,y) != blk:
            distance[x][y-1] = distance[x][y]+1
    
    return way

while True:
    try:
        if __name__ == "__main__":
            String = sys.stdin.readline().strip().split()

            Row = int(String[0][0])
            Col = int(String[0][1])

            Ax = int(String[1][0])
            Ax = int(String[1][1])
            Bx = int(String[2][0])
            Bx = int(String[2][1])

            num_block = int(String[3])

            blocks = []
            for n in range(4,num_block+4):
                block = (String[n][0],String[n][1])
                blocks.append(block)
    except:
        break
