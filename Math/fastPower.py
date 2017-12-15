# -*- coding:utf-8 -*-

# 快速幂运算的核心思想是反复平方法，将幂指数表示为2的幂次的和
# 等价于二进制的进位操作，例如，x^22 = x^16 * x^4 * x^2

def fastPower(x, n, mod):
    res = 1 % mod;
    while (n > 0):
        if (n & 1) != 0:
            res = res * x % mod
            x = x * x % mod
            n >>= 1
    return res