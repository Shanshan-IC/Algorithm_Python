# -*- coding:utf-8 -*-
# 通过一趟扫描将要排序的数据分割成独立的两部分,
# 其中一部分的所有数据都比另外一部分的所有数据都要小,
# 然后再按此方法对这两部分数据分别进行快速排序,整个排序过程可以递归进行,
# 以此达到整个数据变成有序序列

def partition(l, start, end):
    middle = l[start]
    while (start < end):
        while (start<end and l[end] > middle):
            end = end-1
        l[start] = l[end]
        while (start<end and l[start] <= middle):
            start = start+1
        l[end] = l[start]
    l[start] = middle
    return start

def quick_sort(l, start, end):
    if (start < end):
        middle = partition(l, start, end)
        quick_sort(l, start, middle-1)
        quick_sort(l, middle+1, end)
    return l;

def main():
    l = [2, 3, 4, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = quick_sort(l, 0, len(l) - 1)
    print li

main()
