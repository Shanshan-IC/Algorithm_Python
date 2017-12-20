# -*- coding:utf-8 -*-

"""
如果给出 [1,2,0], return 3
如果给出 [3,4,-1,1], return 2

桶排序，A[i]里放着i+1
"""

class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        i, n = 0, len(A)
        while i < n:
            j = A[i]
            if j < 0 or j > n:
                i+= 1
            elif j != i+1:
                if j != A[j-1]:
                    A[i], A[j-1] = A[j-1], A[i]
                else:
                    i += 1
            else:
                i += 1
        for x in xrange(n):
            if A[x] != x + 1:
                return x + 1
        return n + 1