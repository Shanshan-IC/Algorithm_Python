# -*- coding:utf-8 -*-

"""
longest common substring
Reverse SS and become S'S'
​​ . Find the longest common substring between SS and S'S'
​​ , which must also be the longest palindromic substring.

give A = "ABCD", B = "CBCE", return 2

动态规划
"""

def LCS(s, p):
    if not (s and p):
        return 0
    n, m = len(s), len(p)
    dp = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == p[j]:
                dp[i+1][j+1] = 1 + dp[i][j]

    return max(map(max, dp))
