"""
与Majority Number 1相似。但我们要保存2个number.

1. 遇到第一个不同的值，先记录number 2.

2. 新值与n1,n2都不同，则cnt1,cnt2都减少

3. 当n1,n2任意一个为0时，从新值中挑出一个记录下来。

4. 最后再对2个候选值进行查验，得出最终的解。
"""

class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        n1, n2, c1, c2 = None, None, 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 += 1
            elif c2 == 0:
                n2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        return n1 if c1 > c2 else n2