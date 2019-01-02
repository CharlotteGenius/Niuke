#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 18:07:22 2018

@author: xiangyinyu
"""
import sys
files = {}
name_rows = []
while True:
    try:
        string = sys.stdin.readline().strip().split(' ')
        direc = string[0]
        #--------------------------------------------
        name = direc.split('\\')[-1][-16:]
        '''
        The \ character is called an escape character, 
        which interprets the character following it differently. 
        For example, n by itself is simply a letter, 
        but when you precede it with a backslash, it becomes \n, 
        which is the newline character.
        '''
        # record the name of file within 16bits
        #--------------------------------------------
        row = string[-1]
        # record the row number of file, it's a string type!!!
        #--------------------------------------------
        name_row = name+' '+row
        
        if name_row not in files.keys():
            name_rows.append(name_row)
            files[name_row]=1
        else:
            files[name_row] = files[name_row]+1
        # record name and row number in files
        #--------------------------------------------
    except:
        break

for item in name_rows[-8:]:
    sys.stdout.write(item+' '+str(files[name_row])+'\n')
    