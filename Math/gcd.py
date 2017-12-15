# -*- coding:utf-8 -*-

# 最大公约数
"""
常用的方法是辗转相除法，也叫做欧几里得算法
gcb(a, b)是a,b的最大公约数，假设a>b,
a = b*p+q，则gcb(b, q)既能整除b，又能整除a
如此反复就可以得到gcb(a,b)=gcb(c,0)
当第二个数为0的时候返回c
如果a<b，则gcb(b,a%b)=gcb(b,a)=gcb(a,b%a)
"""

def gcb(a, b):
    if b == 0:
        return a
    return gcb(b, a % b)

"""
应用：
给定两个坐标P1(x1, y1)和P2(x2, y2)，求线段P1P2之间除了P1,P2以外还有几个整数点
(y-y1)/(x-x1) = (y2-y1)/(x2-x1)
若M=gcb(x2-x1, y2-y1)，则有x-x1是(x2-x1)/M的整数倍大小，则与M-1个整数坐标点
"""
