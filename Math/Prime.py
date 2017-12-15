# -*- coding:utf-8 -*-

"""
素数系列

"""

import math

class Prime:
    def isPrime(self, x):
        i = 2
        while (i * i <= x):
            if (x % i == 0):
                return False
        return x != 1
