# -*- coding:utf-8 -*-

# 插入排序就是每一步都将一个待排数据按其大小插入到已经排序的数据中的适当位置，直到全部插入完毕。
# 插入排序方法分直接插入排序和折半插入排序两种，这里只介绍直接插入排序

def insert_sort(l):
    for i in range(1,len(l)):
        if (l[i]<l[i-1]):
            temp = l[i]
            j = i
            while (j>0 and l[j-1]>temp):
                l[j] = l[j-1]
                j = j-1
            l[j] = temp
    return l