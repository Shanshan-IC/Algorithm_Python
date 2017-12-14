# -*- coding:utf-8 -*-
# 原理是临近的数字两两进行比较,按照从小到大或者从大到小的顺序进行交换,
# 这样一趟过去后,最大或最小的数字被交换到了最后一位,
# 然后再从头开始进行两两比较交换,直到倒数第二位时结束

def bubble_sort(l):
    len_l = len(l)
    for i in range(0, len_l-1):
        for j in range(i, len_l):
            if (l[i] > l[j]):
                l[i], l[j] = l[j], l[i]
    return l

def main():
    l = [2, 3, 4, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = bubble_sort(l)
    print li

main()