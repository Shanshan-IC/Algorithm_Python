# -*- coding:utf-8 -*-
"""
假设列表从小到大排列，查询一个数字，使用二分法的思想
"""

def binary_search(list, val):
    left = 0
    right = len(list)-1
    while (left<=right):
        mid = left+(right-left)/2
        if val == list[mid] :
            return mid
        elif val < list[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1

if __name__ == '__main__':
    print binary_search([1, 2, 3, 5, 6, 7, 101010, 1928394, 10299283, 28282829338474], 1928394)