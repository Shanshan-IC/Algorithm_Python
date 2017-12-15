# -*- coding:utf-8 -*-

"""
素数系列
埃式筛法：计算整数n以内素数的个数
剔除从小到大的素数的整数倍数，剩下的都是素数

"""

import math

class Prime:
    def isPrime(self, x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i == 0):
                return False
        return x != 1

    def getDivisor(self, x):
        res = []
        for i in range(1, int(math.sqrt(x))+1):
            if (x % i == 0):
                res.append(i)
                if (i != x / i):
                    res.append(i)
        res.sort()

    # sieve (1, n]
    def sieve(self, n):
        primes = []
        isprimes = [True] * n
        isprimes[0] = False
        isprimes[1] = False
        for i in range(2, n+1):
            if (self.isPrime(i)):
                primes.append(i)
                for j in range(i*2, n, i):
                    isprimes[j] = False
        return primes, isprimes
