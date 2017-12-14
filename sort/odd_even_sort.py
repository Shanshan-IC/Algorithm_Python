# -*- coding:utf-8 -*-

# 又一个比较性质的排序,基本思路是奇数列排一趟序,偶数列排一趟序,再奇数排,再偶数排,直到全部有序

def odd_even_sort(l):
    flag = True
    flag = True
    for i in range(len(l) - 1):
        if flag:
            flag = False
            for j in range(1, len(l), 2):
                if l[j] > l[j + 1]:
                    flag = True
                    l[j], l[j + 1] = l[j + 1], l[j]
            for j in range(0, len(l) - 1, 2):
                if l[j] > l[j + 1]:
                    flag = True
                    l[j], l[j + 1] = l[j + 1], l[j]

def main():
    l = [2, 3, 4, 1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = odd_even_sort(l)
    print li

main()