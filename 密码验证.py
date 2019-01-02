#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:03:14 2018

@author: xiangyinyu
"""


# =============================================================================
# 密码要求:
# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有相同长度超2的子串重复
# =============================================================================

def check_psw(psw):
    if len(psw)>8:
    # 要求1——————————————————————————————————————————————————————————————
        upper = ''.join([x for x in psw if x.isupper()])
        lower = ''.join([x for x in psw if x.islower()])
        digit = ''.join([x for x in psw if x.isdigit()])
        char = ''.join([x for x in psw if not (x.isalpha() or x.isdigit())])
        types = [upper, lower, digit, char] 
        if types.count('')<=1:
        # 要求2——————————————————————————————————————————————————————————————
            for l in range(3,len(psw)):
                # l is the length of slices
                for a in range(len(psw)):
                    for b in range(a+2,len(psw)):
                        s1 = psw[a:a+l]
                        s2 = psw[b:b+l]
                        # compare the two slices in psw
                        if s1==s2:
                            return False
                            # 不满足要求3
            # 要求3————————————————————————————————————————————
            return True
            # 三个要求都满足啦！
        else:
            return False
            # 不满足要求2
    else:
        return False
        # 不满足要求1
output = []
while True:
    psw = input()
    if not psw:
        break
    
    if check_psw(psw):
        output.append('OK')
    else:
        output.append('NG')

for out in output:
    print(out)

