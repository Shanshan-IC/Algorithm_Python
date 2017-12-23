# -*- coding:utf-8 -*-
'''
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
'''

class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hash = {}
        for i in xrange(len(numbers)):
            tmp = target - numbers[i]
            if tmp in hash:
                return [hash[tmp], i]
            hash[numbers[i]] = i
        return []