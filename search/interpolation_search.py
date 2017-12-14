# -*- coding:utf-8 -*-
"""
比如要在取值范围1 ~ 10000 之间 100 个元素从小到大均匀分布的数组中查找5，
会考虑从数组下标较小的开始查找。
经过以上分析，折半查找这种查找方式，还是有改进空间的，并不一定是折半的！
mid = （low+high）/ 2, 即 mid = low + 1/2 * (high - low);
改进为下面的计算机方案（不知道具体过程）：
mid = low + (key - a[low]) / (a[high] - a[low]) * (high - low)，
也就是将上述的比例参数1/2改进了，根据关键字在整个有序表中所处的位置，让mid值的变化更靠近关键字key，
这样也就间接地减少了比较次数。

"""

def interpolation_search(list, val):
    len_list = len(list)
    left = 0
    right = len_list-1
    while (left <= right):
        pos = left + (val-list[left])/(list[right]-list[left])*(right-left)
        if (list[pos] == val):
            return pos
        elif (list[pos] > val):
            right = pos - 1
        else:
            left = pos + 1
    return -1;

if __name__ == '__main__':
    print interpolation_search([1, 2, 3, 5, 6, 7, 101010, 1928394, 10299283, 28282829338474], 1928394)