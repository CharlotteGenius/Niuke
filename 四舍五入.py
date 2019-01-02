# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
# 如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
# 四舍五入
import math
# 向上取整 用 ceil()
# 向下取整 用 floor()
# 四舍五入  round()
# 三种的返回结果都是浮点型

n = float(input())
# =============================================================================
# print(math.ceil(n))
# print(math.floor(n))
# print(round(n))
# =============================================================================

# 有个问题是 当输入4.5时，floor()的输出为4而不是5

low_n = math.floor(n)
if n - low_n >= 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))