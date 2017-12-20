# -*- coding:utf-8 -*-
# 什么是旋转数组？

# 比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

# 先找到开始变换的位置
# 该位置左边翻转，后边翻转，最后整体翻转

class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums[0] < nums[-1]:
            return
        pos = 0
        l = len(nums)
        for i in xrange(0, l - 1):
            if nums[i] > nums[i + 1]:
                pos = i
                break
        self.reverse(nums, 0, pos)
        self.reverse(nums, pos + 1, l - 1)
        self.reverse(nums, 0, l - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1