#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:45:19 2018

@author: xiangyinyu
"""

# 编写一个函数，求一个数的二进制表示中的1位的个数，
# 例如9的二进制表示为1001，1位的个数为2。

# =============================================================================
# n = int(input("Please enter the decimal number:"))
# # input a number
# 
# n_binary = bin(n)
# print(n_binary)
# =============================================================================

# 这个方法输出的二进制数前会有前缀“0b”


# another way to convert decimal to binary
n_decimal = int(input("Please enter the decimal number:"))

print("{:b}".format(n_decimal))

# 这个方法更直观，因为没有前缀“0b”



# ctrl + 4 is to multiple comment; ctrl + 5 to inverse


# 下面这个程序是上面的逆

# =============================================================================
# n = input("Please enter the binary number:")
# # input a binary number
# 
# n_dec = int(n,2)
# # 2 is to set the base of the number as 2, so binary
# # int() is to convert it into decimal
# print(n_dec)
# =============================================================================


