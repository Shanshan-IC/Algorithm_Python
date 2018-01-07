# 这个题目的问题在于字符串较长时使用long型会溢出
# 需要取模 (a*b)%m = a % m * b % m
# hashcode(abc) = (a*33^2 + b*33 + c) % m
#               = (33(33(33*0+a)+b)+c)%m

class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        if not key or len(key) == 0:
            return -1
        res = 0
        for a in key:
            res = res * 33 + ord(a)
            res %= HASH_SIZE
        return res

