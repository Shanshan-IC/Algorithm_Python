# -*- coding:utf-8 -*-

# 顾名思意,就是直接从待排序数组里选择一个最小(或最大)的数字,每次都拿一个最小数字出来,
# 顺序放入新数组,直到全部拿完

def selection_sort(l):
    for i in range(0, len(l)):
        min_index = i
        min_num =  l[i]
        for j in range(i+1, len(l)):
            if (l[j] < min_num):
                min_index = j
                min_num = l[j]
        l[min_index] = l[i]
        l[i] = min_num
    return l

def main():
    l = [2, 3, 4, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = selection_sort(l)
    print li

main()