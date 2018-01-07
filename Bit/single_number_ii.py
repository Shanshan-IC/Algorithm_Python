"""
我们把数组中数字的每一位累加起来对3取余，剩下的结果就是那个单独数组该位上的数字，
由于我们累加的过程都要对3取余，那么每一位上累加的过程就是0->1->2->0，换成二进制的表示为00->01->10->00
用a, b来表示01两个数，则初始状态，a = 0, b = 0
00->01->10->00 变成了 a=0, b=0 -> a=0, b=1 -> a=1, b=0 -> a=1, b=1
为了实现
"""


class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        a, b = 0, 0
        for num in A:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b