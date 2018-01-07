# -*- coding:utf-8 -*-


# 两个相同的数做 ^ 异操作结果为0，离题为single number

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

# and
c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c

# or
c = a | b;        # 61 = 0011 1101
print "Line 2 - Value of c is ", c

# xor
# 0^0=0， 1^0=1， 0^1=1， 1^1=0
c = a ^ b;        # 49 = 0011 0001
print "Line 3 - Value of c is ", c

# 逆运算
c = ~a;           # -61 = 1100 0011
print "Line 4 - Value of c is ", c

# a * 2^2
c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c

# a / (2^2)
c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c


# 获得最大的整数Int
print (1<<31) - 1
# 获得最小的整数
print -(1 << 31)
# 最大的long
print (1L << 127) - 1

n = 7
x = 3
# n * 2 ^ x
print n << x
# 整除 n / 2 ^ x
print n >> x

# 判断两个数字是否相等
print (a ^ b) == 0
# 判断奇偶性
print (n&1) == 1

# 两个数进行交换
a ^= b
b ^= a
a ^= b

# 返回绝对值
(x ^ (x >> 31)) - (x >> 31)

# 返回两个数的最大值
b & ((a-b) >> 31) | a & (~(a-b) >> 31)
# 返回两个数的最小值
a & ((a-b) >> 31) | b & (~(a-b) >> 31)

# 判断两个数是不是同正或同负
(a ^ b) >= 0

# flip the sign
a = ~a + 1

# 计算2的n次方
1 << n

# 判断一个数是不是2的n次方
n > 0 and (n & (n-1)) == 0

# 返回平均数
(a + b) >> 1

m = 3
# Get the mth bit of n (from low to high)
(n >> (m-1)) & 1

# Isolate (extract) the right-most 1 bit
x & (-x)
# Isolate (extract) the right-most 1 bit
~x & (x+1)
# Set the right-most 0 bit to 1
x | (x+1)
# Set the right-most 1 bit to 0
x & (x-1)

# n + 1
-~n
# n - 1
~-n

#Get the negative value of a number
~n+1

# if (x == a) x = b; if (x == b) x = a;
x = a ^b ^x


